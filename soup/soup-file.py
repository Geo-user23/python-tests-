import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#Ignore SSL certificate errors 
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter -')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

#Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))

    #beautifulsoup library scrapes webpages the easy way 
    # put in html get back tags
    # scrape data to check a system , check your own data , or a search engine