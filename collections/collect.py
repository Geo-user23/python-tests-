fname = input('Enter File: ')
if len(fname) < 1 : fname = 'clown.txt'
hand = open(fname)

di = dict()
for lin in hand:
    lin = lin.strip()
    #print(lin)
    wds = lin.split()
    #print(wds)
    for w in wds:
        #idiom: retrieve/create/update counter
        di[w] = di.get(w,0) + 1
        print(w,di[w])

print(di)


#this is what happens iniside idiom
 #if w in di :
            #di[w] = di[w] + 1 
        #else:
            #di[w] = 1
            #print('8new8')
        #print(w,di[w])


# now we find most common word by looping through

largest = -1
theword = None
for k,v in di.items() :
    #print (k,v)
    if v > largest :
        largest = v #value
        theword = k #capture/remember word that is largest
print(theword,largest)
