# this program is designed for 2 people who are splitting bills evenly (50% - 50%)
# the program lets each user input the bills they paid individually, total them up, 
# then gives an amount owed by the person who spent less on bills



from datetime import datetime

now = datetime.now() # gets date/ time in the following format: 2021-05-06 13:36:49.706922

user1Amounts= [0., 0., 0., 0., 0., 0., 0., 0., 0., 0.] # array to hold user1's bill amounts   max of 10 bills
user1Bills = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '] # array to hold string labeling what bill was paid  max of 10 bills
user2Amounts= [0., 0., 0., 0., 0., 0., 0., 0., 0., 0.] # array to hold user1's bill amounts   max of 10 bills
user2Bills = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '] # array to hold string labeling what bill was paid  max of 10 bills

#method verifies that input is a string and returns the value if so
def verifyAndGetName():
    userInput = str(input(" What is person 1's name? "))
    while userInput.isalpha() == False: # if userInput is a string
        print ("***** ERROR ***** ")
        print (" Please enter a name (with letters) ")
        userInput = str(input(" What is person 1's name? "))
        if userInput.isalpha == True: 
            break
    return userInput


def verifyAndGetBillName(userName):
    userInput = str(input(" What is the name of the bill you want to add for " + userName + "? "))
    while userInput.isalpha() == False: # if userInput is a string
        print ("***** ERROR ***** ")
        print (" Please enter a bill name (with letters) ")
        userInput = str(input(" What is the name of the bill you want to add for " + userName + "?  "))
        if userInput.isalpha == True: 
            break
    return userInput


print (now) # displays the current date/ time
print (" This program will have each user input their bills and amounts ")
print (" This program is designed to have each user end up paying the same amount (50% - 50%) ")

user1Name = verifyAndGetName()
# user2Name = str(input(" What is person 2's name? "))

def roundOneYesNoErrorCheck(userInput, userName):
    while userInput != 'y' and userInput != 'Y' and userInput != 'n' and userInput != 'N': # while input is a valid character
        print ("********** ERROR **********") # display error message if input is not a valid character
        print (" The character can only be y or n ")
        userInput = str(input(" Would you like to enter bills for " + userName + "? y/n "))
    return userInput

def againYesNoErrorCheck(userInput, userName):
    while userInput != 'y' and userInput != 'Y' and userInput != 'n' and userInput != 'N': # while input is a valid character
            print ("********** ERROR **********") # display error message if input is not a valid character
            print (" The character can only be y or n ")
            userInput = str(input(" Would you like to enter another bill for " + userName + "? y/n "))
    return userInput

#this method gets bill names and amounts from user and stores them in arrays
def getBills(userName, userAmount, userBills):
    index = 0
    count = 0
    userContinue = str(input(" Would you like to enter bills for " + userName + "? y/n "))

    userContinue = roundOneYesNoErrorCheck(userContinue, user1Name) # check to see if input was a valid character

    while userContinue == 'y' or userContinue == 'Y':
        if count == 0: # first prompt for bill input
            userBills[index] = verifyAndGetBillName(userName)
            userAmount[index] = float(input(" What is the amount that " + userName + " paid for " + userBills[index] + "? "))
            # print (" %s paid $ %f for %s " % (userName, userAmount[index], userBills[index]))      this works, but prints out extra decimal values
            print(userName + " paid $" + str(round(userAmount[index], 2)) + " for " + str(userBills[index])) # prints output in the correct $ format
            count += 1
            index += 1
        if count > 0 and count < 10:
           userContinue = input(str (" Would you like to enter another bill for %s? y/n" % (userName)))

        userContinue = againYesNoErrorCheck(userContinue, user1Name) # check to see if input was a valid character

        if userContinue == 'n' or userContinue == 'N': # if user selected to not continue
            break 
        userBills[index] = str(input(" What is the name of the bill you want to add for " + userName + "? "))
        userAmount[index] = float(input(" What is the amount that " + userName + " paid for " + userBills[index] + "? "))
        print(userName + " paid $" + str(round(userAmount[index], 2)) + " for " + str(userBills[index])) # prints output in the correct $ format
        count += 1
        index += 1
    return userAmount, userBills

getBills(user1Name, user1Amounts, user1Bills) # method call for user1 bills and amounts



i = 0
emptyValue = 0.
while user1Amounts[i] != emptyValue:
    moneyFormat = str(round(user1Amounts[i], 2))
    print (" %s : $%s " % (user1Bills[i], moneyFormat))
    i += 1
