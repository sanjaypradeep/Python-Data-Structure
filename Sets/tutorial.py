# SETS #

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


# if you want to delete a element from the list, there're two possiblities,
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






