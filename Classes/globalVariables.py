

import math



class AreaOfCircle():
    PI_VALUE = 3.14

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def areaCalculation(self, radius):
        return 3.14 * (radius**2)


# sampleObj = AreaOfCircle()

# print(sampleObj)

# value = sampleObj.areaCalculation(5)

# print(value)

# what is the class attributes the?

# print(AreaOfCircle.PI_VALUE)

# print(sampleObj.PI_VALUE)

###############

ramObj = AreaOfCircle('Ram', 'Male')

print(ramObj.name)
print(ramObj.gender)


# how about this?

print(AreaOfCircle.name)