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
