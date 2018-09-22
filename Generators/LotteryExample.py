__author__ = 'Sanjay'

# How to create a generator in Python?
# It is fairly simple to create a generator in Python. It is as easy as defining a normal function with
# yield statement instead of a return statement.
#
# If a function contains at least one yield statement (it may contain other yield or return statements),
# it becomes a generator function. Both yield and return will return some value from a function.
#
# The difference is that, while a return statement terminates a function entirely, yield statement pauses the function
#  saving all its states and later continues from there on successive calls.
#

import random
import time

def lottery():
    # returns 6 numbers between 1 and 40
    for i in range(6):
        yield random.randint(1, 40) #bascially yield always returns the value.

    # returns a 7th number between 1 and 15
    time.sleep(10)
    yield random.randint(100,110) #after completing the above iterations, pointer comes here, yeilds returns the value from random.randint(1,15)

print (lottery()) #this really prints the generator object id

# if you want to get all Lottery() values, iterate it.

for random_number in lottery():
       print("And the next number is... %d!" %(random_number))