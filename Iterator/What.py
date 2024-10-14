'''
Iterators are everywhere in Python. 

They are implemented within for loops, comprehensions, generators etc. but are hidden in plain sight.

Points to remember,
1. If a variable is called <iterator.object> then it means it has values inside to iterate upon.
2. two special methods are __iter__() and __next__() - called as iterator protocol.
3. An object can be called iterator only when it's iterable. 
'''


# As mentioned in 3rd point

sampleEmployees = ['ram', 'sanjay', 'london', 'chennai']
# Now above sampleEmployees is a list variable, right? print(type(sampleEmployees))

# Is it iterable? Yes - Because it has bunch of elements to bring them out. isn't it?
# How do we iterate? We normally go on "FOR" loop.

# Creating iterator object now, 
sampleEmployees = iter(sampleEmployees)
print(sampleEmployees) # this tell you that, it's <list_iterator object >

# for i in sampleEmployees:
#     print(i)


# Iterating Through an Iterator
# We use the next() function to manually iterate through all the items of an iterator. 
# When we reach the end and there is no more data to be returned, it will raise the StopIteration Exception. 

sampleNum = [1,2,3]
iterSampleNump = iter(sampleNum)

print(next(iterSampleNump))
print(next(iterSampleNump))
print(next(iterSampleNump))

print(next(iterSampleNump)) # this will throw you a stop iteation error


# You may ask a question, how different is this? for loop does the same. isn't it?

# for item in iterable:
    # add anything as per the need..

# Can you think how this above `for` loop is implemented internally.

# create an iterator object from that iterable
iter_obj = iter(iterable)

# infinite loop
while True:
    try:
        # get the next item
        element = next(iter_obj)
        # do something with element
    except StopIteration:
        # if StopIteration is raised, break from loop
        break


# So internally, the for loop creates an iterator object, iter_obj by calling iter() on the iterable.

# Ironically, this for loop is actually an infinite while loop.

# Inside the loop, it calls next() to get the next element and executes the body of the for loop with this value. 
# After all the items exhaust, StopIteration is raised which is internally caught and the loop ends. 
# Note that any other kind of exception will pass through.



# Have you ever thought? why to make an iterator ?

# Iterators allow you to make an iterable that computes its items as it goes. 
# means that you can make iterables that are lazy, in that they don’t determine what their next item is until you ask them for it.


# Usage of iterator instead of a list, set, or another iterable data structure can sometimes allow us to save memory


# Can you convert a non-iterable object into iterator?

sampleInt = 90

# print(iter(sampleInt)) 
# Exception has occurred: TypeError
# 'int' object is not iterable

# NO