class StudentInfo:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def fullName(self):
        return ('{} {}'.format(self.first, self.last))

    def setIdNumber(self):
        self.idNumber = (input("%s, what is your ID number? " % (self.first)))
    
    def getIdNumber(self):
        return self.idNumber

    def setEmail(self):
        self.email = (self.last + '.'+ self.first[0] + self.idNumber + '@yourSchool.com')
    
    def setGrades(self):
        i = 0
        grade = int
        self.grades = []
        while grade :
            grade = int(input("Please enter grade #%d " % (i + 1)))
            self.grades.append(grade)
            i += 1
            proceed = str(input("Would you like to enter another grade? (y or n)"))
    
    
    def printAllInfo(self):
        print("First Name .... ", self.first)
        print("Last Name ..... ", self.last)
        print("ID Number ..... ", self.idNumber)
        print("Email ......... ", self.email)
    
    


Student1 = StudentInfo('Jon', 'Doe')

# Student1.setGrades()
Student1.setIdNumber()
Student1.setEmail()

Student1.printAllInfo()



