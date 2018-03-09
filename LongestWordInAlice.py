def Alice():
    alice = open('Alice.txt', 'r')
    WORD = ('')
    for l in alice:
        words = l.replace(',','').replace('_','').replace('?','').replace('[',' ').replace(']','').replace('(','').replace(')','').replace('"','').replace('!','').split()
        #Replaces all the given values
        for i in words:
            if len(i) > len(WORD):#Checks if the len of the longest word is less than the word, if so replaces the longest word
                WORD = i
            else:
                continue
    alice.close()
    print('%s has %s characters.' %(WORD, len(WORD)))

Alice()
