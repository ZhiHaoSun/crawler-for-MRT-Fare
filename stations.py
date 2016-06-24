import json

content = ""
with open('stations.json', 'r') as content_file:
    content = content_file.read()
bus_stations = json.loads(content)
result = {}

for code in bus_stations.keys():
	fullname = bus_stations[code].strip()
	name = fullname.split('-')[1].strip()
	result[name] = code

write_stations = open('station_names.json' , 'wb')
write_stations.write(json.dumps(result))