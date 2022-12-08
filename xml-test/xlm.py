import xml.etree.ElementTree as ET

input = '''
<stuff>
        <users>
            <user x="2">
                <id>001</id>
                <name>Tom</name>
            </user>
            <user x="7">
                <id>009</id>
                <name>Rob</name>
            </user>
        </users>
    </stuff>'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print('User count:', len(lst))
#this print gives you the amount of users

#itterates through children of users
for item in lst:
    print('Name', item.find('name').text)
    print('id', item.find('id'.text))
    print('Attribute', item.get("x")) #x attribute


    #extensible markup language 
    #designed to store and transport data 
    #self-descriptive
