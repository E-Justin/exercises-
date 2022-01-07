# Write a function that reverses a string. The input string is given as an array of characters s

s = ["J","u","s","t","i","n"]
length = len(s)

def reverseString(s):
    
    i = 0
    j = length -1

    while i < length / 2:
        front = s[i]
        back = s[j]
        s[i] = back
        s[j] = front
        i += 1
        j -= 1
    return s

reverseString(s)

i = 0
while i < length:
    print(s[i])
    i += 1
    
# or .........

def reverseString2(str):
    str = str[::-1]
    return str
