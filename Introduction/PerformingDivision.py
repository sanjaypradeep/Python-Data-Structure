__author__ = 'Sanjay'
# Task
# Read two integers and print two lines. The first line should contain integer division, aa//bb. The second line should contain float division, aa/bb.
#
# You don't need to perform any rounding or formatting operations.
#
# Input Format
# The first line contains the first integer, aa. The second line contains the second integer, bb.
#
# Output Format
# Print the two lines as described above.
#
# Sample Input
#
# 4
# 3
# sample Output
#
# 1
# 1.3333333333333333

# Enter your code here. Read input from STDIN. Print output to STDOUT
from __future__ import division

a = int(raw_input())
b = int(raw_input())

print a//b
print a/b
