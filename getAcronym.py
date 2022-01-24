# this program creates an acronym when given a string

# get user input
userInput = (str(input(" Type in a phrase to get its acronym ")))

def getAcronym(userString):
    # convert string into a list
    userString = userString.split()

    i = 0
    acronym = ''
    while i < (len(userString)): # while i is less than the length of the list
        acronym += userString[i][0]# get first letter of each word
        i += 1

    acronym = acronym.upper() # convert to uppercase

    print(acronym)

getAcronym(userInput)
