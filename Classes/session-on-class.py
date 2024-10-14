

class Employee():

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.pi = 3.142

    # wrong way for gettting employee name from the object.
    # def getEmployeeName(self, inputFromUser):
    #     print("Employee name is ", inputFromUser)

    def getNewEmployeeName(self):
        print("new employee name is ", self.name)

    def getEmployeeAge(self):
        print(self.name + "'s age is " + self.age)

import random

class Bank():
    def __init__(self, name, age, dob, address):
        self.name = name
        self.age = age
        self.dob = dob
        self.address = address
        self.accountNumber = random.randint(1,1000)
        self.accountBalance = 0
        print("Your account got created, " + self.name)

    
    def getCustomerAccountInfo(self):
        print("Hello " + self.name)
        print("Your account got created, here's your account number " , str(self.accountNumber))
        print("Your current balance of your account is ", str(self.accountBalance))

    def getMyBirthDate(self):
        print('Hello ' + self.name + ' you birthday is ' + self.dob)


ramIsTheCustomer = Bank('Ram', 26, '1/1/2020', 'London')

ramIsTheCustomer.getCustomerAccountInfo()

ramIsTheCustomer.getMyBirthDate()



ram = Employee("Ram")
san = Employee("Sanjay")

print(ram)
print("--------")
# print(ram.getEmployeeName("Ram"))

ram.getNewEmployeeName()

san.getNewEmployeeName()
sanjay.getEmployeeAge()




class EmployeeV2():
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def getEmployeeName(self):
        return("Employee name is " + self.name)
