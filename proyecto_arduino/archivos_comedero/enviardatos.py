import datetime
import sys
import serial
import time
import os
import pytz



ser = serial.Serial('/dev/ttyACM0', baudrate=9600, timeout=1.0)

while True:
	try:
		try:
			ser.write("a")
		except Exception:
			print("Error")

	except serial.SerialException as e:
		print("There is no new data from serial port")