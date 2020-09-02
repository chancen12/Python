import json
json_data='{"name":"chance","age":"25","location":"Kigali"}'
d=json.loads(json_data)
print(d)
print(d.values())