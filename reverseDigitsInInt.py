# reverse integer

x = 1534236469


def reverseInt(x) -> int:
    if x < 0: # if negative
        negative = True
        x = abs(x) # get abs (take away negative sign)
    else: # if positive
        negative = False

    x = str(x) # convert to string

    x = x[:: -1] # reverse string

    x = int(x) # convert back to an int

    if negative == True: # if original value was negative
        x = 0 - x # get negative equivalent of reversed value

    return (x)

print (reverseInt(x))


#   or .......

# reverse an integer

x = -123


def reverseInt2(int):
    reversedNumber = 0
    negative = False
    if int == 0: # if argument is 0
        return 0 # return 0
        

    if int < 0: # if x is negative
        negative = True
        int = abs(int) # get absolute value (remove negative sign)

    while int != 0: # while int is not 0
        remainder = int % 10 # ÷ by 10 and get remainder

        reversedNumber = (reversedNumber * 10) + remainder # math to reverse int one digit at a time

        int = int // 10 # divide by 10 and truncate the decimal (if there is one)

    if negative == True: # if the original argument was negative
        reversedNumber = -abs(reversedNumber) # put the negative sign back at the front

    print (reversedNumber) # print reversed number
    return int # return reversed int

reverseInt2(x) # function call
