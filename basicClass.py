class StudentInfo:
    # counstructor
    def __init__(self, first, last):
        self.first = first
        self.last = last

    # method to return full name
    def fullName(self):
        return ('{} {}'.format(self.first, self.last))

    # method to set idNumber
    def setIdNumber(self):
        self.idNumber = (input("%s, what is your ID number? " % (self.first)))
    
    # method to get id number
    def getIdNumber(self):
        return self.idNumber

    # method to set email up
    def setEmail(self):
        self.email = (self.last + '.'+ self.first[0] + self.idNumber + '@yourSchool.com')
    
    # method to have user input their grades
    def setGrades(self):
        i = 0
        grade = int
        self.grades = []
        while grade :
            grade = int(input("Please enter grade #%d " % (i + 1)))
            self.grades.append(grade)
            i += 1
            proceed = str(input("Would you like to enter another grade? (y or n)"))
            if proceed == "n" or proceed == "N":
                break
    
    # method to calculate grade average
    def calculateAverage(self):
        length = len(self.grades) # get length
        sum = 0 # set sum to 0
        for i in range(length):
            sum += self.grades[i] # sum all of grades
        
        self.average = sum / (length) # return the average
        

    # method to print all info
    def printAllInfo(self):
        print("First Name .... ", self.first)
        print("Last Name ..... ", self.last)
        print("ID Number ..... ", self.idNumber)
        print("Email ......... ", self.email)
        print("Grade average ... ", self.average)
    
    


Student1 = StudentInfo('Jon', 'Doe')
Student1.setIdNumber()
Student1.setEmail()
Student1.setGrades()
Student1.calculateAverage()


Student1.printAllInfo()



