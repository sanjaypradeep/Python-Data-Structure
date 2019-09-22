# SETS #

# 1. Set() - elements in the set will be in un-ordered type
# 2. Cannot have duplicate value.

print(dir(set))

# Results in - ['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '_
# _ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__',
# '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '
# __reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__
# subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection',
# 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference',
# 'symmetric_difference_update', 'union', 'update']'


# empty set creation

sampleSet = set()
print(sampleSet) # set()
# the above example prints an empty set

sampleSet.add("Sun")
sampleSet.add("moon")

print(sampleSet) # {'moon', 'Sun'}
# the above output shows, two elements which got added to a empty set.
# note : {} cannot be a empty set, it can only mean a empty dictionary, always empty set is gonna be set()

sampleSet.clear()
print(sampleSet)
# output is set() -because all the elements inside the set is cleared.

# if you want to add multiple elements in a single line, below is the solution.
sampleSet.update([1, 2, 3, 'testing'])

# if you want to get desired element from the set, then normally, you'll pass it's index value as input. Isn't it?

# print(sampleSet[2])

# you will get an error
# TypeError: 'set' object does not support indexing


# if you want to delete a element from the set, there're two possiblities,
# 1. discard
# 2. remove

print(sampleSet)
sampleSet.discard('testing')
print(sampleSet) # {1, 2, 3}


sampleSet.remove(3)
print(sampleSet) # {1, 2}

# I'm gonna try discarding/removing element which isn't available inside the set.

sampleSet.discard('test') # returns nothing / no error will be thrown

# sampleSet.remove('test') # throws you KeyError: 'test'

####### Lesson : 2 ##########

s1 = {'one', 'two', 'three', 'four'}
s2 = {1, 2, 3, 4}

#above are the two variables s1 and s2, whose type is <class 'set'>
print(type(s1)) # <class 'set'>
print(type(s2)) # <class 'set'>

# 1. Comparing two sets and finding the difference in elements.

print(s1.difference(s2)) # {'four', 'three', 'one', 'two'}

# Explanation :  Checks each element in s1 is present in s2 or not, will print only those elements which aren't
# available, therefor here it prints all the elements, hence it's not available.

s1.add(4) # now added one more element into s1.
print(s1) # {'two', 4, 'one', 'four', 'three'}

print(s1.difference(s2)) # {'two', 'one', 'four', 'three'}

print(s2.difference(s1)) # {1, 2, 3} -because '4' available in s1, therefore it's printing elements which aren't as diff

# 2. ------------- difference_update - updates a set in-place rather than return a new one. ----------------

A = {'a', 'c', 'g', 'd'}
B = {'c', 'f', 'g'}

result = A.difference_update(B)

print('A = ', A) # A =  {'d', 'a'}
print('B = ', B) # B =  {'c', 'g', 'f'}
print('result = ', result) # result =  None


# 3. -----------Union - Union is performed using | operator. Same can be accomplished using the method union().

# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# use | operator
# Output: {1, 2, 3, 4, 5, 6, 7, 8}
print(A | B)


# 4. ----------- Intersection is performed using & operator. Same can be accomplished using the method intersection().

# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# use & operator
# Output: {4, 5}
print(A & B)

# 5. ------ Symmetric Diffrence

# Symmetric Difference of A and B is a set of elements in both A and B except those that are common in both.
# Symmetric difference is performed using ^ operator. Same can be accomplished using the method symmetric_difference().


# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# use ^ operator
# Output: {1, 2, 3, 6, 7, 8}
print(A ^ B)


# 6. ----- intersection_update

# The intersection_update() allows arbitrary number of arguments (sets).
# This method returns None (meaning, absence of a return value). It only updates the set calling the intersection_update() method.


A = {1, 2, 3, 4}
B = {2, 3, 4, 5}

result = A.intersection_update(B)

print('result =', result)
print('A =', A)
print('B =', B)

# Example 2: intersection_update() with Two Parameters

A = {1, 2, 3, 4}
B = {2, 3, 4, 5, 6}
C = {4, 5, 6, 9, 10}

result = C.intersection_update(B, A)

print('result =', result)
print('C =', C)
print('B =', B)
print('A =', A)



# 7. ------- isDisjoint()

# The isdisjoint() method returns True if two sets are disjoint sets. If not, it returns False.
# Two sets are said to be disjoint sets if they have no common elements.

A = {1, 2, 3, 4}
B = {5, 6, 7}
C = {4, 5, 6}

print('Are A and B disjoint?', A.isdisjoint(B))
print('Are A and C disjoint?', A.isdisjoint(C))


# Example 2: isdisjoint() with Other Iterables as arguments

A = {'a', 'b', 'c', 'd'}
B = ['b', 'e', 'f']
C = '5de4'
D ={1 : 'a', 2 : 'b'}
E ={'a' : 1, 'b' : 2}

print('Are A and B disjoint?', A.isdisjoint(B))
print('Are A and C disjoint?', A.isdisjoint(C))
print('Are A and D disjoint?', A.isdisjoint(D))
print('Are A and E disjoint?', A.isdisjoint(E))


# 8. ------------issubset

# The issubset() method returns True if all elements of a set are present in another set (passed as an argument).
# If not, it returns False.

A = {1, 2, 3}
B = {1, 2, 3, 4, 5}
C = {1, 2, 4, 5}

# Returns True
print(A.issubset(B))

# Returns False
# B is not subset of A
print(B.issubset(A))

# Returns False
print(A.issubset(C))

# Returns True
print(C.issubset(B))



# 9. ------ isSuperset

# The issuperset() method returns True if a set has every elements of another set (passed as an argument). If not, it returns False.

A = {1, 2, 3, 4, 5}
B = {1, 2, 3}
C = {1, 2, 3}

# Returns True
print(A.issuperset(B))

# Returns False
print(B.issuperset(A))

# Returns True
print(C.issuperset(B))