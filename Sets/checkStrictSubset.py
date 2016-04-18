__author__ = 'Sanjay'
#
# Example:
#  Set([1,3,4])
# ([1,3,4])
#  is a strict superset of set([1,3])
# ([1,3])
# .
#  Set([1,3,4])
# ([1,3,4])
#  is not a strict superset of set([1,3,4])
# ([1,3,4])
# .
#  Set([1,3,4])
# ([1,3,4])
#  is not a strict superset of set([1,3,5])
# ([1,3,5])
# .
#
#
# Input Format
#
#
# The first line contains the space separated elements of set A
# A
# .
#  The second line contains integer N
# N
# , the number of other sets.
#  The next N
# N
#  lines contains the space separated elements of the other sets.
#
# Constraints
#
# 0<len(set(A))<501
# 0<len(set(A))<501
#
# 0<N<21
# 0<N<21
#
# 0<len(otherSets)<101
# 0<len(otherSets)<101
#
#
#
#
# Output Format
#
#
# Print True if set A
# A
#  is a strict superset of all other N
# N
#  sets. Otherwise, print False.
#
#
# Sample Input
#
# 1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78
# 2
# 1 2 3 4 5
# 100 11 12
#
#
#
# Sample Output
#
# False
#
#
#
# Explanation
#
#
# Set A
# A
#  is the strict superset of the set([1,2,3,4,5])
# ([1,2,3,4,5])
#  but not of the set([100,11,12])
# ([100,11,12])
#  because 100
# 100
#  is not in set A
# A
# .
#  Hence, the output is False.

print [all([A > B for B in [set(raw_input().split()) for _ in xrange(int(raw_input()))]]) for A in [set(raw_input().split())]][0]