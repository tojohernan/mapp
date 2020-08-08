from influxdb import InfluxDBClient

json_body = [
		{
        "measurement": "cpu_load_short",
        "tags": {
            "host": "server01",
            "region": "us-west"
        },
        "fields": {
            "value": 0.64
        }
    }
]

client = InfluxDBClient('localhost', 8086, 'root', 'root', 'example')

client.create_database('example')

client.write_points(json_body)

result = client.query('select value from cpu_load_short;')

print("Result: {0}".format(result))