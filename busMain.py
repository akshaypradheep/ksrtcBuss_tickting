#!/usr/bin/python3
import pyrebase
import serial
import lcddriver
from time import *
lcd = lcddriver.lcd()
rf = serial.Serial('/dev/ttyUSB0')
busRoute = "thrissur-chlkara"
dir = "up"
#Firebase Configuration
config = {
  "apiKey":"AIzaSyDk7u7EP1vx4Rp1WGckMr_ouWQXT0ity6Q",
  "authDomain": "ksrtc-d07e0.firebaseapp.com",
  "databaseURL": "https://ksrtc-d07e0.firebaseio.com",
  "storageBucket": "ksrtc-d07e0.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()
#-------------------------------------------------------------
def fireRead(barcod):
	_name = db.child("Name").child(barcod).get()
	_route = db.child("Route").child(barcod).get()
	return _name.val(), _route.val()

def inRead():
	a = rf.read(12)
	y = a.decode('utf-8')
	print(y)
	#a = input("enter the user ID:")
	return y

def display(name,route):
        lcd.lcd_clear()
        lcd.lcd_display_string(name,1)
        lcd.lcd_display_string(route,2)
	

def timeStamp():
	import datetime
	now = datetime.datetime.now()
	a = str(now.day) + "-" + str(now.month) + "-" + str(now.year)
	return a 
	pass

def mark(_usr):
		_us = str(_usr)
		a = db.child("date").child(_us).child(timeStamp()).child(busRoute).child(dir).get()
		_a = a.val()
		print(_a)
		if _a == "1":
			return "not allowed"
			pass
		else:	
			db.child("date").child(_usr).child(timeStamp()).child(busRoute).child(dir).set("1")
			return "Marked"

#--------------------------------------------------------------
while True:
	_u = inRead()
	a,b = fireRead(_u)
	if a is None:
		display("not allowed","not registered")
	else:
		display(a,b)
		_x = mark(_u)
		sleep(1.5)
		lcd.lcd_clear()
		lcd.lcd_display_string("      KSRTC", 1)
		lcd.lcd_display_string(_x, 2)
		
		pass
