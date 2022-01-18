# this method takes a list of ints as its argument
# converts list to an int
# adds 1 to int
# converts int back into a list and returns the value

def plusOne(digits):
    number = map(str, digits) # convert each element into a character
    number = ''.join(number) # convert list of chars to a single string
    number = int(number) # convert string to int
    print(type(number))
    number += 1

    number = str(number) # convert back to string
    number = map(int, number) # convert each character to an int
    number = list(number) # convert back to list

    return number
  
# Runtime: 16 ms
# Memory Usage: 13.6 MB
