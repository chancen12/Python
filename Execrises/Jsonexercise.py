import  json

people_string='''
{
    "people":[
        {
            "name":"John Smith",
           "phone":"0771-002-420",
           "emails":"chanc@gmail.com",
           "haslicense":"false"
        },
        {
            "name":"Kaze David",
           "phone":"0771-002-340",
           "emails":null,
           "haslicense":"true"        
        }


            ]
}
'''
data=json.loads(people_string)

#print(type(data ['people']))
for i in  data['people']:
    #print(i['name'])
    del i['phone']
new_string=json.dumps(data,indent=2)
print(new_string)
#print(type(new_string))
