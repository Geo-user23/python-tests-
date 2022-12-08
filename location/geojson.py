import urllib.request, urllib.parse, urllib.error
import json


serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'


while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    url = serviceurl + urllib.parse.urlencode(
        {'address': address})

    
    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'character')

    try:
        js = json.loads(data)
    except:
        js = None

        #checks the status good for debugging
    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

#dumps pretty prints it 
    print(json.dumps(js, indent=4))

    #parse then break down code to get what you want

    lat = js['results'] [0] ['geometry'] ['location'] ['lat']
    lng = js['results'] [0] ['geometry'] ['location'] ['lng']
    print('lat', lat, 'lng', lng)
    location = js['results'] [0] ['formatted_address']
    print(location)

    #use google maps api
    #need an api key