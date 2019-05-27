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
