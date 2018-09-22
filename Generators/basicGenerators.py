# Generators are very easy to implement, but a bit difficult to understand.
#
# Generators are used to create iterators, but with a different approach. Generators are simple functions which return an
# iterable set of items, one at a time, in a special way.
#
# When an iteration over a set of item starts using the for statement, the generator is run.
# Once the generator's function code reaches a "yield" statement, the generator yields its execution back to the for loop, ' \
# returning a new value from the set. The generator function can generate as many values (possibly infinite) as it wants,' \
#  yielding each one in its turn.

# simple example of a generator function which returns 7 random integers

# What are generators in Python?
# There is a lot of overhead in building an iterator in Python; we have to implement a class with __iter__() and __next__() method,
# keep track of internal states, raise StopIteration when there was no values to be returned etc.
#
# This is both lengthy and counter intuitive. Generator comes into rescue in such situations.
#
# Python generators are a simple way of creating iterators. All the overhead we mentioned above are automatically handled by generators in Python.
#
# Simply speaking, a generator is a function that returns an object (iterator) which we can iterate over (one value at a time).


import random
import time

def lottery():
    # returns 6 numbers between 1 and 40
    for i in range(6):
        yield random.randint(1, 40) #bascially yield always returns the value.

    # returns a 7th number between 1 and 15
    time.sleep(10)
    yield random.randint(100,110) #after completing the above iterations, pointer comes here, yeilds returns the value from random.randint(1,15)

# print (lottery())

for random_number in lottery():
       print("And the next number is... %d!" %(random_number))