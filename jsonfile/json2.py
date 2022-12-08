import json 

input = '''
[
    { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
    },
    { "id" : "009",
    "x" : "7",
    "name" : "Chuck"
    }
]  '''

#load the string parses and turns into python list 
info = json.loads(input)
print('User count:', len(info))

#iterates through dictionary 
for item in info:
    print('Name', item['name'])
    print('Id', item['id'])
    print('Attribute', item['x'])

#this is json but python treats it as a list 