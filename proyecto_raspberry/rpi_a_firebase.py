import json
import time
import urllib2

from firebase import firebase 
import Adafruit_DHT # Para leer la temperatura del DHT11



#### Inicializo variables #### 
firebase = firebase.FirebaseApplication('https://comedero-9f39f.firebaseio.com/', None)

sensor = Adafruit_DHT.DHT11
pin_dht11 = 23
data_backup = [ ]




def internet_connection():
    try:
        urllib2.urlopen('http://www.google.com', timeout=1)
        return True
    except urllib2.URLError as err: 
        return False

def cargar_backup():
	n=0
	for data in data_backup:
		n=n+1
		result = firebase.post('mediciones/', data)
		print (result)
	print ("Se cargaron ", n ," datos de backup...")

def control_temperatura(): # Necesito hacer el control y la lectura por separados
	datos_sin_enviar=False
	global data_backup

	while True:
		humidity, temperature = Adafruit_DHT.read_retry(sensor, pin_dht11)
		data_new = {
			"ts": time.time(),
			"temp":  temperature,
			"hum":  humidity
		}

		 
		if internet_connection() == True:
			if datos_sin_enviar==True:
				cargar_backup()
				datos_sin_enviar=False
				
				data_backup= []
				with open('data_backup.json', 'w') as f:
					json.dump(data_backup, f)
					f.close()
				print (data_backup)
				print('SE VACIA BACKUP')

			if humidity is not None and temperature is not None:
				result = firebase.post('mediciones/', data_new)
				print(result)
				print(data_new)
			else:
			    print('Fallo en la lectura!')

		else:
			datos_sin_enviar=True
			data_backup.append(data_new)
			with open('data_backup.json', 'w') as f:
				json.dump(data_backup, f)
				f.close()
			print('Se cargo nueva data en backup: ')
			print (data_backup)

		time.sleep(10)

try:
	control_temperatura()
except KeyboardInterrupt:                #Si el usuario pulsa CONTROL+C...
    print "quit"                         #Avisamos del cierre al usuario