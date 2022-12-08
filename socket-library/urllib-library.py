import urllib.request
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())


#since HTTP is common urllib does all socket work 
#page look like a file 
#does not show header but you can change that

#counts = dict()
#for line in fhand:
#words = line.decode().split()
#for word in words:
    #coun[word] = counts.get(word,0) + 1
#print(counts)

#you can also do python functions