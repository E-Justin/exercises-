class Employee:
    #constructor
    def __init__(self, first, last, pay, employeeNumber):
        self.first = first
        self.last = last
        self.pay = pay
        self.employeeNumber = employeeNumber
        #self.email = ('%s.%s.%s@yourCompany.com' % (last,first,employeeNumber))
        self.email = (last + '.' + first + str(employeeNumber) + '@yourCompany.com')
    
    # class method to get full name of employee
    def fullName(self):
        return ('{} {}'.format(self.first, self.last))

# must initialize them in order this way
employee_1 = Employee('Jon', 'Doe', 75000, 12345)

#employee_1.first = 'Jon'
#employee_1. last = 'Doe'
#employee_1.pay = 75000
#employee_1.employeeNumber = 1234f




def printItems(classInstance):
    print('First Name........... %s' % (classInstance.first))
    print('Last Name............ %s' % (classInstance.last))
    print('Pay.................. %s' % (classInstance.pay))
    print('Employee Number ..... %d' % (classInstance.employeeNumber))
    print('Email ............... %s' % (classInstance.email))

printItems(employee_1)
print(employee_1.fullName())

