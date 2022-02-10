birthdays = {
    'Justin' : '09/09',
    'Charli' : '06/29',
    'Kristen' : '06/17',
    'Michael' : '05/19',
    'James' : '12/21',
    'Britney' : '08/18',
    'John' : '10/15'

}

def menu():
    print("~~~~~~ Birthdays ~~~~~~")
    print("Press 1: to find a birthday")
    print("Press 2: to add a name and birthday to the list")
    print("Press 3: to see all names in the birthday dictionary")
    print("Press 0: to exit")
    userInput = int(input())
    return userInput

def selections(userInput):
    if userInput == 3: 
        for line in birthdays:
            print(line) # prints each key of the dictionary
    if userInput == 1:
        name = str(input("Enter a name "))
        name = name.capitalize()
        print("%s's birthday : %s" % (name, birthdays[name])) # prints out name and brithday
    if userInput == 2: 
        name = str(input("What is the name of the person who you want to add a birthday for? "))
        name = name.capitalize() # capitalizes the first letter and the rest are lowercase
        bday = str(input("What is their birthday? mm/dd"))
        birthdays[name] = bday
        print("Birthday dictionary updated ")


while True:
    userInput = menu()
    if userInput == 0:
        break
    selections(userInput)

#print('Charli' in birthdays.keys())     check to see if a key exists: returns T or F
#print('09/09' in birthdays.values())    check to see if a value exists: returns T or F
