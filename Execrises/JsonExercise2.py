import json

with open('JsonFile.json') as f:
  data=json.load(f)
  print(data)  

#for s in data['states']:
    #print(s)

