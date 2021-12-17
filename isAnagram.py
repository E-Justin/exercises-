# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
s = "anagram"
t = "margana"


def isAnagram(s, t):
    anagram = False # set boolean variable to false
    reversed = s[::-1] # reverses s

    if (t == reversed): # if it is an anagram
        anagram = True
    else: # if it is not an anagram
        anagram = False

    return anagram


print (isAnagram(s,t))
