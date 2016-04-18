__author__ = 'Sanjay'
#
# You are given two sets, A
# A
#  and B
# B
# .
#  Your job is to find whether set A
# A
#  is a subset of set B
# B
# .
#
#  If set A
# A
#  is subset of set B
# B
# , print True.
#  If set A
# A
#  is not a subset of set B
# B
# , print False.
#
#
# Input Format
#
#
# The first line will contain the number of test cases, T
# T
# .
#  The first line of each test case contains the number of elements in set A
# A
# .
#  The second line of each test case contains the space separated elements of set A
# A
# .
#  The third line of each test case contains the number of elements in set B
# B
# .
#  The fourth line of each test case contains the space separated elements of set B
# B
# .
#
#
# Constraints
#
# 0<T<21
# 0<T<21
#
# 0<Number of elements in each set<1001
# 0<Number of elements in each set<1001
#
#
# Output Format
#
#
# Output True or False for each test case on separate lines.
#
#
# Sample Input
#
# 3
# 5
# 1 2 3 5 6
# 9
# 9 8 5 6 3 2 1 4 7
# 1
# 2
# 5
# 3 6 5 4 1
# 7
# 1 2 3 5 6 8 9
# 3
# 9 8 2
#
#
#
# Sample Output
#
# True
# False
# False
#
#
#
# Explanation
#
#
# Test Case 01 Explanation
#
# Set A
# A
#  = {1 2 3 5 6}
#  Set B
# B
#  = {9 8 5 6 3 2 1 4 7}
#  All the elements of set A
# A
#  are elements of set B
# B
# .
#  Hence, set A
# A
#  is a subset of set B
# B
# .

for i in range(int(raw_input())): #More than 4 lines will result in 0 score. Blank lines won't be counted.
    a = int(raw_input()); A = set(raw_input().split())
    b = int(raw_input()); B = set(raw_input().split())
    print not bool(A.difference(B))