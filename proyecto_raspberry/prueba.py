import json
import time

from firebase import firebase 

firebase = firebase.FirebaseApplication('https://comedero-9f39f.firebaseio.com/', None)

data_backup = []

data_new = {
		"ts": time.time(),
		"temp":  30,
		"hum":  40
	}

for i in range (1,10):
	data_backup.append(data_new)

	with open('data_backup.json', 'w') as f:
	    json.dump(data_backup, f)

	f.close()
	print('Se cargo nueva data en backup: ')
	print (data_backup)
	time.sleep(0.5)

result = firebase.post('mediciones/', data_backup)
print(result)

#json_str = json.dumps(data)
#data_string = json.dumps(data)
#print (data)
#print (data_string)

#data.append(data_nueva)
#print (data)

#with open('data_backup.json', 'r') as f:
#     data_bk = json.load(f)
#     dataappend data_backup

#with open('data_backup.json', 'w') as f:
#     json.dump(data_bk, f)