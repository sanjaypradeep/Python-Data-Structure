__author__ = 'Sanjay'

# Differences between Generator function and a Normal Iterator function

# Here is how a generator function differs from a normal function.
#
# Generator function contains one or more yield statement.

# When called, it returns an object (iterator) but does not start execution immediately.

# Methods like __iter__() and __next__() are implemented automatically. So we can iterate through the items using next().

# Once the function yields, the function is paused and the control is transferred to the caller.

# Local variables and their states are remembered between successive calls.

# Finally, when the function terminates, StopIteration is raised automatically on further calls.


def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n


a = my_gen()
print (a)
next(a) # This is printed first
next(a) # This is printed second
next(a) # This is printed at last

# next(a) # StopIteration because there's no more n value available to bring out.

# One interesting thing to note in the above example is that, the value of variable n is remembered between each call.
#
# Unlike normal functions, the local variables are not destroyed when the function yields. Furthermore, the generator object can be iterated only once.
#
# To restart the process we need to create another generator object using something like a = my_gen().

# Note: One final thing to note is that we can use generators with for loops directly.

# Here you go ..

for item in my_gen():
    print (item)

# Here's the output

# This is printed first
# 1
# This is printed second
# 2
# This is printed at last
# 3