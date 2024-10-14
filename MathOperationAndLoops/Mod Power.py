__author__ = 'Sanjay'

# Task
# You are given three integers: aa, bb, and mm, respectively. Print two lines.
# The first line should print the result of pow(a,b). The second line should print the result of pow(a,b,m).
#
# Input Format
# The first line contains aa, the second line contains bb, and the third line contains mm.
#
# Constraints
# 1?a?101?a?10
# 1?b?101?b?10
# 2?m?10002?m?1000
#
# Sample Input
#
# 3
# 4
# 5
# Sample Output
#
# 81
# 1
from __future__ import division

a = int(raw_input())
b = int(raw_input())
m = int(raw_input())

t = pow(a,b)

print t
print t % m