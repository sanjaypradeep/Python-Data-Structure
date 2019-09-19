# ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__',
# '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__',
# '__imul__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__',
# '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '
# __subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse',
# 'sort']

animals = ['Tiger', 'Lion', 'Dog', 'Zebra']

# create an empty List

# __add__(self, element) - to concatinate two list and make a single list
sampleNumbers = [13,4356,65,4776]
print(sampleNumbers.__add__(animals)) #print(sampleList) => [13, 4356, 65, 4776, 'Tiger', 'Lion', 'Dog', 'Zebra']


# __contains__ - check whether the element is available in list or not.
print(animals.__contains__('Mouse')) #False
print(animals.__contains__('Lion')) #True


# __delattr__ - delete element in the list, by supplying its index value
# sampleNumbers.__delattr__(13)
# print(sampleNumbers)

#__delitem__ - delete item from the list,  by supplying its index value
sampleNumbers.append(4)
print(sampleNumbers)
sampleNumbers.__delitem__(1) # 4356 will be removed, whose index value is 1
print(sampleNumbers)

# __eq__ - to compare two list and returns bool value (True or false)
print(sampleNumbers.__eq__(animals)) # false

# __format__ -
print(sampleNumbers.__format__('')) # '[13, 65, 4776, 4]'
print(type(sampleNumbers.__format__(''))) # <class 'str'>


seg = ""




