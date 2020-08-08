
#!/usr/bin/python
import serial
import time
import os
from datetime import datetime
ser = serial.Serial('/dev/ttyACM1', baudrate=9600, timeout=1.0)
#ser = serial.Serial('/dev/ttyACM0', 9600)

while 1 :
	try:
		val = ser.readline().replace("\r\n","")
		url = 'curl -i -XPOST \'http://localhost:8086/write?db=distancia\' --data-binary \'distancia value='+val+'\''





		print url
		os.system(url)
		time.sleep(1)

		
	except serial.SerialException as e:
		print("There is no new data from serial port")