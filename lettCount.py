def wordcount(w):
    wc = {}
    for letter in w:  #Makes the dictonary into one what has all the different letters
        wc[letter] = 0

    for k, v in wc.items():  #goes through each set of the dictonary
        
        for letter in w:  #Finds the letter in banana again, because the loop before stops at the last letter
            
            if letter == k:  #Only adds a value to the total ammount if the leter that it is looped to(letter) is equal to the first value of the set
                v += 1
                wc[k] = v  #Channges the normal value to the new value
    print ('These are the character in the word %s\n\n%s' %(w, wc))

wordcount('banana')
