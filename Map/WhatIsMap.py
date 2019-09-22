# Python map() function
# map() function returns results as Map object type, after applying the given function to each item of a
# given iterable (list, tuple etc.)

# Parameters :

# fun : It is a function to which map passes each element of given iterable.
# iter : It is a iterable which is to be mapped.


# Python program to demonstrate working
# of map.

# Return double of n
def addition(n):
    return n + n


# We double all numbers using map()
numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(result) # this will return an object.

print(set(result)) # {8, 2, 4, 6}

print(tuple(result)) # returns empty tuple as () - because when you contruct a tuple from a map object, then it returns empty tuple.

print(list(result)) # returns empty list as [] - because when you contruct a list from a map object, then it returns empty list.

print(result) # map object



def addingTwoNumber(m,n):
    return m+n


firstT = (1, 2, 3, 4, 5) # whose len is 5
secondT = (4, 5, 6, 9) # whose len is 4

# here's the map calculation, map(<methodName>, param1, param2)
print(list(map(addingTwoNumber, firstT, secondT))) # output as - [5, 7, 9, 13]

# here the para1 is supplied as list, but still it works and gives the same output.
print(list(map(addingTwoNumber, firstT, list(secondT)))) # output as - [5, 7, 9, 13]

# We can also use lambda expressions with map to achieve above result.
# Here's the example,
print(list(map(lambda x,y: x+y, firstT, secondT)))

# Double all numbers using map and lambda

numbers = (1, 2, 3, 4)
result = map(lambda x: x + x, numbers)
print(list(result))


# One more example..
# Add two lists using map and lambda

numbers1 = [1, 2, 3, 4, 5]
numbers2 = [4, 5, 6]

result = map(lambda x, y: x + y, numbers1, numbers2)
print(list(result))

# List of strings
l = ['sat', 'bat', 'cat', 'mat']

# map() can listify the list of strings individually
test = tuple(map(list, l))
print(test)


l = ['sanjay', 'surya']
op = list(map(tuple, l))
print(op)



l = ['sanjay', 'surya']
op = list(map(list, l))
print(op)

overAllList = []
for listParam in op:
    for values in listParam:
        overAllList.append(values)

print(overAllList)
dictOutput = {}
for i in overAllList:
    dictOutput[i] = overAllList.count(i)

print(dictOutput)


# Here's the single line approach.
print({i: overAllList.count(i) for i in overAllList})


