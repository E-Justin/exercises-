# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

s = "aabb"


def findFirstNonRepeat(s):
    i = 0
    length = len(s) # get length of string

    while i < length and i != -1: # while index is within range
        x = s[i]
        count = s.count(x)
        if count == 1: # if no repeated chars have been found
            break # exit loop
        else:
            i += 1
    if i == length: # if method has run through length of the string and not found a duplicate
        i = -1
    

    return i # return index of non repeating char (or -1 if there are only repeating characters)


print(findFirstNonRepeat(s))
