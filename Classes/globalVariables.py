

import math

class Circle():
    PI_VALUE = 3.14
        
    def calculate_area(self, radius):
        return PI_VALUE * (self.radius**2)

class CustomClass():

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender




# sampleObj = AreaOfCircle()

# print(sampleObj)

# value = sampleObj.areaCalculation(5)

# print(value)

# what is the class attributes the?

# print(AreaOfCircle.PI_VALUE)

# print(sampleObj.PI_VALUE)

###############

ramObj = CustomClass('Ram', 'Male')

print(ramObj.name)
print(ramObj.gender)
