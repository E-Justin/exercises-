# this program is designed for 2 people who are splitting bills evenly (50% - 50%)
# the program lets each user input the bills they paid individually, total them up, 
# then gives an amount owed by the person who spent less on bills



from datetime import datetime

now = datetime.now() # gets date/ time in the following format: 2021-05-06 13:36:49.706922

user1Amounts= [0., 0., 0., 0., 0., 0., 0., 0., 0., 0.] # array to hold user1's bill amounts   max of 10 bills
user1Bills = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '] # array to hold string labeling what bill was paid  max of 10 bills
user2Amounts= [0., 0., 0., 0., 0., 0., 0., 0., 0., 0.] # array to hold user1's bill amounts   max of 10 bills
user2Bills = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '] # array to hold string labeling what bill was paid  max of 10 bills
user1total = 0
user2total = 0

def getTotals(userAmounts):
    i = 0
    total = 0
    while userAmounts[i] != 0. and i < 10:
        total += userAmounts[i]
        i += 1
    return total

#method verifies that input is a string and returns the value if so
def verifyAndGetName(userNumber):
    userInput = str(input(" What is person %d's name? " % userNumber))
    while userInput.isalpha() == False: # if userInput is not a string
        print ("***** ERROR ***** ")
        print (" Please enter a name ")
        userInput = str(input(" What is person %d's name? " % userNumber))
        if userInput.isalpha == True: # if it is a string
            break
    return userInput

# this method verifies and gets the bill name
def verifyAndGetBillName(userName):
    userInput = str(input(" What is the name of the bill you want to add for " + userName + "? "))
    while userInput.isalpha() == False: # if userInput is a string
        print ("***** ERROR ***** ")
        print (" Please enter a bill name ")
        userInput = str(input(" What is the name of the bill you want to add for " + userName + "?  "))
        if userInput.isalpha == True: # if userInput is a number
            break
    return userInput


print (now) # displays the current date/ time
print (" This program will have each user input their bills and amounts ")
print (" This program is designed to have each user end up paying the same amount (50% - 50%) ")

user1Name = verifyAndGetName(1)
user2Name = verifyAndGetName(2)

# verifies that character entered is expected y/n for the first time
def roundOneYesNoErrorCheck(userInput, userName):
    while userInput != 'y' and userInput != 'Y' and userInput != 'n' and userInput != 'N': # while input is a valid character
        print ("********** ERROR **********") # display error message if input is not a valid character
        print (" The character can only be y or n ")
        userInput = str(input(" Would you like to enter bills for " + userName + "? y/n "))
    return userInput

# verifies that character entered is expected y/n for the second and so on times
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

    userContinue = roundOneYesNoErrorCheck(userContinue, user1Name) # check to see if input was a valid , if so, store it in userContinue

    while userContinue == 'y' or userContinue == 'Y': # if the user wishes to continue
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
getBills(user2Name, user2Amounts, user2Bills) # method call for user1 bills and amounts

user1total = getTotals(user1Amounts)
user2total = getTotals(user2Amounts)
print("\n")
print (" %s's total amount in bills paid is %s " % (user1Name, str(round(user1total, 2))))
print (" %s's total amount in bills paid is %s " % (user2Name, str(round(user2total, 2))))
print("\n")

def whoOwesWho(user1Name, user2Name, user1total, user2total):
    file = open ("pythonDataFile.txt", "a+") # open for appending / creates file if it does not exist

    if user1total > user2total: # if user1 paid more in bills
        difference = user1total - user2total
        amountOwed = difference / 2
        file.write ("%s owes %s $%d \n" % (user2Name, user1Name, amountOwed))
    if user1total < user2total: # if user2 paid more in bills
        difference = user2total - user1total
        amountOwed = difference / 2
        file.write ("%s owes %s $%d \n" % (user1Name, user2Name, amountOwed))
    else:
        amountOwed = 0
        file.write ("Each person paid the same amount in bills this month \n")
    file.close()

def writeDataToFile(userName, userBills, userAmounts):
    file = open ("pythonDataFile.txt", "a+") # open for appending / creates file if it does not exist
    i = 0
    emptyValue = 0.
    file.write("********** %s's bills for this month **********\n" % userName)
    file.write("Time/ Date : %s \n" % now)
    while user1Amounts[i] != emptyValue and i < len(userBills):
        moneyFormat = str(round(user1Amounts[i], 2))
        file.writelines ("%s : $%s \n" % (user1Bills[i], moneyFormat))   
        i += 1
   
    file.write("\n")
    file.close()

writeDataToFile(user1Name, user1Bills, user1Amounts)
writeDataToFile(user2Name, user2Bills, user2Amounts)
whoOwesWho(user1Name, user2Name, user1total, user2total)
