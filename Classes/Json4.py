import json
d = {'name': "chance", 'age': 45, 'ID': 4}
print("Original String:")
print(json.dumps(d, sort_keys=True, indent=4))