# Each key is separated from its value by a colon (:), the items are separated by commas, and the whole thing is enclosed in curly braces. An empty dictionary without any items is written with just two curly braces, like this: {}.
# Keys are unique within a dictionary while values may not be. The values of a dictionary can be of any type, but the keys must be of an immutable data type such as strings, numbers, or tuples.

# How to create a dictionary with some values?

myDict = {'name': 'AnyName', 'id': 123, 'info': 'value of id not neccessarily need to be string since it has integer as numbers'}

print(myDict) # Output: {'name': 'AnyName', 'id': 123, 'info': 'value of id not neccessarily need to be string since it has integer as numbers'}

print(myDict.keys()) #Output: dict_keys(['name', 'id', 'info'])
