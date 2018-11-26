# This is all about set

# A set is a collection which is unordered and unindexed. In Python sets are written with curly bracket


# Here's the example

# 1. Create a set

mySet = {} # this isn't considered as empty set, type(mySet) --> will say it's a dictionary

mySet = {'apple', 'banana'}

print mySet[1] # this will throw error as "it doesn't support indexing" as mentioned in the description

# 2. get the elements out

for item in mySet:
	print(i)

#output:
# apple
# banana

# 3. Add Items

# if you want to add one element into the set, then proceed like below. 

mySet.add("Cherry")

print (mySet) #{'apple', 'cherry', 'banana'} comes in random order.


# 4. update Items
#  if you want to add many elements in a single shot, try this below. 

mySet.update(['orange', 'pomo', 'mango'])
print (mySet) #{'cherry', 'orange', 'apple', 'pomo', 'banana', 'mango'


# 5. Length of Set

len(mySet) # 6

# 6. Remove Item
# To remove an item in a set, use the remove(), or the discard() method.

mySet.remove('pomo') # this will remove 'pomo' elements from the set, will not return any.
print(mySet) # {'cherry', 'orange', 'apple', 'banana', 'mango'}


mySet.discard("orange")
print (mySet) # {'cherry', 'apple', 'banana', 'mango'}


# You can also use the pop(), method to remove an item, but this method will remove the last item. Remember that sets are unordered, so you will not know what item that gets removed.

# The return value of the pop() method is the removed item.
# here's the custom example.

s1 = {'rob', 'bob', 'alice'}
print (s1)

#when you run the below code, it's expected to remove 'alice', but it'snt

s1.pop() #retured me bob

# its better not use pop()


# how to delete all the elements inside the Set()

mySet.clear() # returns {} empty set



# how to delete the complete set itself?

del mySet


# difference()

s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}

s1.difference(s2) #{1,2,3} 
s2.difference(s1) # {6,7,8}



# symmentric_difference()
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}

s1.symmentric_difference(s2) #{1,2,3,6,7,8}
s2.symmentric_difference(s1) #{1,2,3,6,7,8}


# symmetric_difference_update()	inserts the symmetric differences from this set and another
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}

s1.symmetric_difference_update(s2)
s1 # {1,2,3,6,7,8} 

# if you do s2.symmetric_difference_update(s1) it will return the same elements as above.


# difference_update()	Removes the items in this set that are also included in another, specified set

s1.difference_update(s2) # {1,2,3} -> it actually remvoved 4,5 from s1

s2.difference_update(s1) # {6,7,8} --> it actually removed 4,5 from s2


# Union

s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}

s1 | s2 # {1,2,3,4,5,6,7,8} --> the common items (4,5) between two sets are not repeated


# Intersection

s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}

s1 & s2 # {4, 5} --> returns common elements which are available in two sets


# intersection_update()	- Removes the items in this set that are not present in other, specified set(s)

s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}

s1.intersection_update(s2) 
s1 # {4,5} because it removed not matching elements
s2 # {8, 4, 5, 6, 7} its still the same

s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}

s2.intersection_update(s1)
s1 # {1,2,3,4,5}
s2 # {4,5} because it removed not matching elements








