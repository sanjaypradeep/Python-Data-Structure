# Python map() function
# map() function returns a list of the results after applying the given function to each item of a given iterable (list, tuple etc.)

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
# print(result) #this will return an object.
#
#
# print (set(result)) # {8, 2, 4, 6}

# print (tuple(result))
#
# print (list(result))
#
# print (result)



def addingTwoNumber(m,n):
    return m+n


firstT = (1,2,3,4,5)
secondT = (4,5,6,9)
print(list(map(addingTwoNumber, firstT, secondT)))

print(list(map(addingTwoNumber, firstT, list(secondT))))

# We can also use lambda expressions with map to achieve above result.

# Double all numbers using map and lambda

numbers = (1, 2, 3, 4)
result = map(lambda x: x + x, numbers)
print(list(result))


# One more example..
# Add two lists using map and lambda

numbers1 = [1, 2, 3]
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
print (op)

