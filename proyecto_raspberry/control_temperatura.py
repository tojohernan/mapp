import Adafruit_DHT
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT) ## GPIO 17 como salida
GPIO.setup(27, GPIO.OUT) ## GPIO 27 como salida

pin_ventilacion=17
pin_luz=27

GPIO.output(pin_ventilacion, GPIO.LOW)
GPIO.output(pin_ventilacion, GPIO.LOW)

sensor = Adafruit_DHT.DHT11
pin_dht11 = 23



temperatura_ideal = 20
ventilacion_prendida=False
luz_prendida=False

def estado(sensor,accion):
	if sensor == "v":
		if accion == 1:
			GPIO.output(pin_ventilacion, GPIO.HIGH)
			print ("PIN VENTILADOR ON")
			return()
		else:
			GPIO.output(pin_ventilacion, GPIO.LOW)
			print ("PIN VENTILADOR OFF")
			return()
	else:
		if accion == 1:
			GPIO.output(pin_luz, GPIO.HIGH)
			print ("PIN LUZ ON")
			return()
		else:
			GPIO.output(pin_luz, GPIO.LOW)
			print ("PIN LUZ OFF")
			return()


while True:
	
	humidity, temperature = Adafruit_DHT.read_retry(sensor, pin_dht11)
	#print("Cual es la temperatura actual?")
	#temperature = input()
	print (humidity)
	print (temperature)
	if temperature == temperatura_ideal:
		estado("l", 0)
		luz_prendida=False
		estado("v", 0)
		ventilacion_prendida=False
	else:
		if (temperature < temperatura_ideal-2) and (luz_prendida==False):
			print("Aumentando la temperatura..")
			estado("l",1)
			luz_prendida=True
		else:
			if (temperature > temperatura_ideal+2) and (ventilacion_prendida == False):
				print("Bajando la temperatura..")
				estado("v",1)
				ventilacion_prendida=True
