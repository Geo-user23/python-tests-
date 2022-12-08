import re
hand = open('mbox-short.txt')
numlist = list()
for line in hand:
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)' , line)
    if len(stuff) !=1 : continue
    num = float(stuff[0])
    numlist.append(num)
    print('Maximun:', max(numlist))

    #^ where you start 
    #[0-9] single characters set
    #+ at least one or more 
    #\s space 
    # \$ use slash to find a character