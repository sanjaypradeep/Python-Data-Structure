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


