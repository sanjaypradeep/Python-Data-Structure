__author__ = 'Sanjay'
# Loops are control structures that iterate over a range to perform a certain task.
#
# There are two kinds of loops in Python.
#
# A for loop:
#
for i in range(0,5):
    print i
# And a while loop:
#
i = 0
while i < 5:
    print i
    i+=1
# Here, the term range(0,5) returns a list of integers from 00 to 55: [0,1,2,3,4][0,1,2,3,4].
#
# Task
# Read an integer NN. For all non-negative integers i<Ni<N, print i2i2. See the sample for details.
#
# Input Format
# The first and only line contains the integer, NN.
#
# Constraints
# 1?N?201?N?20
#
# Output Format
# Print NN lines, one corresponding to each ii.
#
# Sample Input
#
# 5
# Sample Output
#
# 0
# 1
# 4
# 9
# 16
# Enter your code here. Read input from STDIN. Print output to STDOUT
from __future__ import division

a = int(raw_input())
#b = int(raw_input())
#c = int(raw_input())
#d = int(raw_input())

for i in range(0,a):
    print i*i
