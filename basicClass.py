
class StudentInfo:
    
    
    # constructor
    def __init__ (self, first, last, gpa, idNumber):
        self.first = first 
        self. last = last
        self.gpa = gpa
        self.idNumber = idNumber
        self.district = "alvaradoISD" # initiated district with a string value
        self.email = (first + '.' + last + str(idNumber) + '@' + self.district + '.net')

        
    # class method to get full name
    def fullName(self):
        return ('{} {}'.format(self.first, self.last) )

    


Student_1 = StudentInfo # class instance
Student_2 = StudentInfo ('Jon', 'Doe', 3.75, 246810) # class instance with values automatically initiated
# or 
# Student_2.first = 'Jon'
# Student_2.last = 'Doe"
# Student_2.gpa = 3.75
# Student_2.idNumber = 246810

# method to have user input student info
def getInfo(classInstance):
    classInstance.first = input("What is your first name? ")
    classInstance.last = input("What is your last name? ")
    classInstance.gpa = input("What is your GPA? ")
    classInstance.idNumber = input("What is your school id  number? ")

# method to print student info
def printInfo(classInstance):
    print("First name ..... %s" % (classInstance.first))
    print("Last name ..... %s" % (classInstance.last))
    print("GPA ........... %s" % (str(classInstance.gpa)))
    print("ID Number ..... %s" % (str(classInstance.idNumber)))
    print("Email ......... %s" % (classInstance.email))


    
print(Student_2.fullName())

printInfo(Student_2)

