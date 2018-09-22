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



def justChecking():
    for tempIteration in range(10):
        yield tempIteration
        # print (i)

justCheckingValues = justChecking() # here the expectation is "a" has the yeild value.

print (a) # print the assinged value. But no, it prints the generator object ID. Example <generator object justChecking at 0x101b18200>

# if you want to print the yeild values, lets again iterate.

for i in justCheckingValues:
    print (i)