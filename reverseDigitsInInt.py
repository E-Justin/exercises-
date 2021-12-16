# program to reverse digits in an int
# dont include zeros
# if x = 0, return 0


x = 120
y = 0

print(x)


def reverseNum(x):
    if x == 0:
        return 0
    size = 0
    y = abs(x)
    while y != 0:
        y = y// 10
        size +=1 # size will hold the number of digits in tht int

    i = -1
    count = 0
    if abs(x) != x: # if number is negative
        x = str(x) # convert to string for easier manipulating
        while count < size:
            if x[i] == 0: # dont include 0
                i -= 1
            if count == 0:
                strX = '-' # attach the - sign at the front
                strX += ''.join(x[i]) # join elements in reverse order
                count += 1
                i -= 1
            else:
                strX += ''.join(x[i]) # join elements in reverse order
                count += 1
                i -= 1
    else: # if number is positive
        x = str(x) # convert to string for easier manipulating
        while count < size:
            if x[i] == 0:
                i -= 1 # dont inlcude 0
            if count == 0:
                strX = ''.join(x[i]) # join elements in reverse order
                count += 1
                i -= 1
            else:
                strX += ''.join(x[i]) # join elements in reverse order
                count += 1
                i -= 1
    return int(strX) # return reversed int
    

    
strX = reverseNum(x)

print(strX)






