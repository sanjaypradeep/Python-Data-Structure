__author__ = 'Sanjay'

# Tuples are data structures that look a lot like lists. Unlike lists, tuples are immutable (meaning that they cannot be modified once created). This restricts their use because we cannot add, remove, or assign values; however, it gives us an advantage in space and time complexities.
#
# A common tuple use is the swapping of 22 numbers:
#
# a,b = b,a
# Here a,ba,b is a tuple, and it assigns itself the values of b,ab,a.
#
# Another awesome use of tuples is as keys in a dictionary. In other words, tuples are hashable.
#
# Task
# You are given an integer, NN, on a single line. The next line contains NN space-separated integers. Create a tuple, TT, of those NN integers, then compute and print the result of hash(TT).
#
# Note: hash() is one of the functions in the __builtins__ module.
#
# Input Format
#
# The first line contains an integer, NN (the number of elements in the tuple).
# The second line contains NN space-separated integers describing TT.
#
# Output Format
#
# Print the result of hash(TT).
#
# Sample Input
#
# 2
# 1 2
# Sample Output
#
# 3713081631934410656

raw_input()
print hash(tuple(map(int, raw_input().strip().split(" "))))
