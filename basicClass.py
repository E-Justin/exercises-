class StudentInfo:
    
    
    # constructor
    def __init__ (self, first, last, idNumber):
        self.first = first 
        self. last = last
        self.idNumber = idNumber
        self.district = "alvaradoISD" # initiated district with a string value
        self.email = (first + '.' + last + str(idNumber) + '@' + self.district + '.net')

        
    # class method to get full name
    def fullName(self):
        return ('{} {}'.format(self.first, self.last) )
    
    def printInfo(self):
        print("First name ..... %s" % (self.first))
        print("Last name ..... %s" % (self.last))
        print("GPA ........... %s" % (str(self.gpa)))
        print("ID Number ..... %s" % (str(self.idNumber)))
        print("Email ......... %s" % (self.email))
    
    def setGrades(self):
        self.gpa = str(input("What is your gpa"))
        return self.gpa

    def getGrades(self):
        print(self, "'s gpa is : ", self.gpa)
    


Student_1 = StudentInfo # class instance
Student_2 = StudentInfo ('Jon', 'Doe', 3.75, 246810) # class instance with values automatically initiated
# or 
# Student_2.first = 'Jon'
# Student_2.last = 'Doe"
# Student_2.gpa = 3.75
# Student_2.idNumber = 246810

# method to have user input student info


# method to print student info

print(Student_2.fullName())

Student_2.printInfo()
