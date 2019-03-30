#!/usr/bin/python3
import serial
rf = serial.Serial('/dev/ttyUSB0')
while True:
	a= rf.read(12)
	y = a.decode('utf-8')
	print(y)
