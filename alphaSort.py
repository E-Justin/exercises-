words = ['zebra', 'apple' , 'corn', 'squash', 'banana', 'dill pickle', 'azle ']

def sort(toSort):
    i = 0
    j = 1
    length = len(toSort) # get length of list

    while i < length: #! while i is in range
        
        if toSort[i] > toSort[j]: #! if words are not in order
            toSort[i], toSort[j] = toSort[j], toSort[i] # swap positions
            
        j += 1 # move to next position
        
        if j == length: #! if j has reached outside of range
            i += 1 # move to next position
            j = i + 1 # set j to the next word (after i)
        if i == length -1: #! if i has reached the last word
            break # exit loop
    
    print(toSort)

sort(words)

        
