import datetime
import sys
import serial
import time
import os
import pytz

from influxdb import InfluxDBClient


#ser = serial.Serial(sys.argv[1], baudrate=9600, timeout=1.0)
ser = serial.Serial('/dev/ttyUSB0', baudrate=9600, timeout=1.0)

while True:
	try:
		try:
			#val = float(ser.readline().replace("\n", "").strip())			
			values_list = ser.readline().split(",")

			if len(values_list) == 2:
				temp = float(values_list[0])
				humedad = float(values_list[1])
			
			print(temp)
			print(humedad)
			
		except Exception:
			print("Error")
		else:
			points = [
				{
					"time": datetime.datetime.utcnow(),
	        		"measurement": "temperatura",
	        		"tags": {
	            		"dispositivo": "Arduino_MEGA"
		        	},
	    	    	"fields": {
	        	    	"temperatura": temp
	        		}
	        	},
	        	{
					"time": datetime.datetime.utcnow(),
	        		"measurement": "humedad",
	        		"tags": {
	            		"dispositivo": "Arduino_MEGA"
		        	},
	    	    	"fields": {
	        	    	"humedad": humedad
	        		}
	        	}
	        ]
	        #ESCRIBO EN INFLUX
			client = InfluxDBClient('localhost', 8086, 'root', 'root', 'flisol')
			client.write_points(points)

			result = client.query('select value from cpu_load_short;')
			#print("Result: {0}".format(result))
	except serial.SerialException as e:
		print("There is no new data from serial port")