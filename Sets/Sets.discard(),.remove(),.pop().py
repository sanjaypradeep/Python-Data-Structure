__author__ = 'Sanjay'

# .remove(x)
# This operation removes element xx from the set.
# If element xx does not exist, it raises a KeyError.
# The .remove(x) operation returns None.
#
# Example
#
# >>> s = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
# >>> s.remove(5)
# >>> print s
# set([1, 2, 3, 4, 6, 7, 8, 9])
# >>> print s.remove(4)
# None
# >>> print s
# set([1, 2, 3, 6, 7, 8, 9])
# >>> s.remove(0)
# KeyError: 0
# .discard(x)
# This operation also removes element xx from the set.
# If element xx does not exist, it does not raise a KeyError.
# The .discard(x) operation returns None.
#
# Example
#
# >>> s = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
# >>> s.discard(5)
# >>> print s
# set([1, 2, 3, 4, 6, 7, 8, 9])
# >>> print s.discard(4)
# None
# >>> print s
# set([1, 2, 3, 6, 7, 8, 9])
# >>> s.discard(0)
# >>> print s
# set([1, 2, 3, 6, 7, 8, 9])
# .pop()
# This operation removes and return an arbitrary element from the set.
# If there are no elements to remove, it raises a KeyError.
#
# Example
#
# >>> s = set([1])
# >>> print s.pop()
# 1
# >>> print s
# set([])
# >>> print s.pop()
# KeyError: pop from an empty set
# Task
# You have a non-empty set ss, and you have to execute NN commands given in NN lines.
#
# The commands will be pop, remove and discard.
#
# Input Format
#
# The first line contains integer nn, the number of elements in the set ss.
# The second line contains nn space separated elements of set ss. All of the elements are non-negative integers, less than or equal to 9.
# The third line contains integer NN, the number of commands.
# The next NN lines contains either pop, remove and/or discard commands followed by their associated value.
#
# Constraints
#
# 0<n<200<n<20
# 0<N<200<N<20
# Output Format
#
# Print the sum of the elements of set ss on a single line.
#
# Sample Input
#
# 9
# 1 2 3 4 5 6 7 8 9
# 10
# pop
# remove 9
# discard 9
# discard 8
# remove 7
# pop
# discard 6
# remove 5
# pop
# discard 5
# Sample Output
#
# 4
# Explanation
#
# After completing these 1010 operations on the set, we get set([4])([4]). Hence, the sum is 44.
#
# Note: Convert the elements of set s to integers while you are assigning them. To ensure the proper input of the set, we have added the first two lines of code to the editor.

n = input()
s = set(map(int, raw_input().split()))
m = int(raw_input())
for _ in xrange(m):
    pair = raw_input().split()
    arg = pair[1] if len(pair) == 2 else ""
    eval("s." + pair[0] + "(" + arg + ")")
print sum(s)