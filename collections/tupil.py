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
        #print(w,di[w])

#print(di)


tmp = list()
for k,v in di.items() :
    new = (v,k)
    tmp.append(new)
    #this has values flipped

    #this sorts it in order from value and word value as well
    tmp = sorted(tmp, reverse=True)
#print('sorted',tmp[:5]) sorts in order leasty to greatest
#prints up to 5 

for v,k in tmp[:5] :
    print(k,v)

#to get descending do tmp = sorted(tmp, reverse=True)
    




