# this program is designed for 2 people who are splitting bills evenly (50% - 50%)
# the program lets each user input the bills they paid individually, total them up, 
# then gives an amount owed by the person who spent less on bills



from datetime import datetime

now = datetime.now() # gets date/ time in the following format: 2021-05-06 13:36:49.706922

user1Amounts= [0., 0., 0., 0., 0., 0., 0., 0., 0., 0.] # array to hold user1's bill amounts   max of 10 bills
user1Bills = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '] # array to hold string labeling what bill was paid  max of 10 bills
user2Amounts= [0., 0., 0., 0., 0., 0., 0., 0., 0., 0.] # array to hold user1's bill amounts   max of 10 bills
user2Bills = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '] # array to hold string labeling what bill was paid  max of 10 bills

print (now) # displays the current date/ time
print (" This program will have each user input their bills and amounts ")
print (" This program is designed to have each user end up paying the same amount (50% - 50%) ")

user1Name = str(input(" What is person 1's name? "))
# user2Name = str(input(" What is person 2's name? "))

#this method gets bill names and amounts from user and stores them in arrays
def getBills(userName, userAmount, userBills):
    index = 0
    count = 0
    userContinue = str(input(" Would you like to enter bills for " + userName + "? y/n "))

    while userContinue != 'y' and userContinue != 'Y' and userContinue != 'n' and userContinue != 'N': # while input is a valid character
        print ("********** ERROR **********") # display error message if input is not a valid character
        print (" The character can only be y or n ")
        userContinue = str(input(" Would you like to enter bills for " + userName + "? y/n "))

    while userContinue == 'y' or userContinue == 'Y':
        if count == 0: # first prompt for bill input
            userBills[index] = str(input(" What is the name of the bill you want to add for " + userName + "? "))
            userAmount[index] = float(input(" What is the amount that " + userName + " paid for " + userBills[index] + "? "))
            # print (" %s paid $ %f for %s " % (userName, userAmount[index], userBills[index]))      this works, but prints out extra decimal values
            print(userName + " paid $" + str(round(userAmount[index], 2)) + " for " + str(userBills[index])) # prints output in the correct $ format
            count += 1
            index += 1
        if count > 0 and count < 10:
           userContinue = input(str (" Would you like to enter another bill for %s? y/n" % (userName)))
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
    print (" %s : $%f " % (user1Bills[i], user1Amounts[i]))
    i += 1
