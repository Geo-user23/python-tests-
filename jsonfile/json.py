import json 

data = '''
{
    "name" : "Chuck",
    "phone" : {
        "type" : "intl",
        "number" : "+1 734 303 4456"
    },
    "email" : {
        "hide" : "yes"
    }
}'''

info = json.loads(data)
print('Name:', info["name"])
print('Hide:', info["email"]["hide"])

#you import json 
#json has key value pairs dictionary, lists, use triple qouted 
#turns into python dictionary  info sub name example
#this is an example of dictionary 