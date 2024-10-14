__author__ = 'Sanjay'
# Task
# Read four numbers, aa, bb, cc, and dd, and print the result of ab+cdab+cd.
#
# Input Format
# Integers aa, bb, cc, and dd are given on four separate lines, respectively.
#
# Constraints
# 1?a?10001?a?1000
# 1?b?10001?b?1000
# 1?c?10001?c?1000
# 1?d?10001?d?1000
#
# Output Format
# Print the result of ab+cdab+cd on one line.
#
# Sample Input
#
# 9
# 29
# 7
# 27
# Sample Output
#
# 4710194409608608369201743232
# Note: This result is bigger than 263?1263?1. Hence, it won't fit in the long long int of C++ or a 64-bit integer.
from __future__ import division

a = int(raw_input())
b = int(raw_input())
c = int(raw_input())
d = int(raw_input())

x = a**b
y = c**d

print x+y