import json
import time

from firebase import firebase


firebase = firebase.FirebaseApplication('https://comedero-9f39f.firebaseio.com/', None)

#POST
temperatura = '25'
humedad = '40'
timestamp = 'ddmmaahhmmss'


data = {
	"temp":  temperatura,
	"ts": time.time()
}

data_json = json.dumps(data)
result1 = firebase.post('mediciones/temperatura', data)
#result2 = firebase.post('mediciones/humedad', humedad)
#result3 = firebase.post('mediciones/timestaml', timestamp)

#GET
#result = firebase.get('/users', None)

print(result1)
#print result2
#print result3