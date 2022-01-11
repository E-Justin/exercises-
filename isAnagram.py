# return true if it is a valid anagram

s = "rat" 
t = "car"

def isAnagram(s, t):
    anagram = True
    
    # get lengths of both arguments
    length1 = len(s) 
    length2 = len(t)
    
    # if lengths are not the same
    if length1 != length2:
        anagram = False

    i = 0
    
    while i < length1 and anagram is True: # while i is in range and anagram is True
        letter = s[i] # get the letter to look at
        if s.count(letter) == t.count(letter): # if there are the same amount of this letter in each word
            i += 1 # continue
        else: # if there are different amounts of this letter in each word
            anagram = False # set to false and exit the loop
    
    return anagram

anagram = isAnagram(s,t)

print(anagram)

# Runtime: 3880 ms
# Memory Usage: 13.7 MB
    
