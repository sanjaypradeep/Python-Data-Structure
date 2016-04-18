__author__ = 'Sanjay'
#
# Task
#
# You are given a two lists A
# A
#  and B
# B
# . Your task is to compute their cartesian product A
# A
# XB
# B
# .
#
# Example
# A = [1, 2]
# B = [3, 4]
#
# AxB = [(1, 3), (1, 4), (2, 3), (2, 4)]
#
#
# Note: A
# A
#  and B
# B
#  are sorted lists, and the cartesian product's tuples should be output in sorted order.
#
#
# Input Format
#
#
# The first line contains the space separated elements of list A
# A
# .
#  The second line contains the space separated elements of list B
# B
# .
#
# Both lists have no duplicate integer elements.
#
# Constraints
#
# 0<A<30
# 0<A<30
#
# 0<B<30
# 0<B<30
#
#
# Output Format
#
#
# Output the space separated tuples of the cartesian product.
#
#
# Sample Input
#
#  1 2
#  3 4
#
#
#
# Sample Output
#
#  (1, 3) (1, 4) (2, 3) (2, 4)
#

a=map(int,raw_input().split(" "))
b=map(int,raw_input().split(" "))
from itertools import product
for i in list(product(a,b)):
    print i,