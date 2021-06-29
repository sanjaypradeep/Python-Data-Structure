__author__ = 'Sanjay'
# /*
# You are given two integers. Store them into two variables and then exchange them. Rather than using any fancy logic, make sure to use a tuple to do the task. Print the two numbers.
#
# Input Format
#
# Two integers on separate lines.
#
# Output Format
#
# Two integers on separate lines.
#
# Sample Input
#
# 2
# 1
# Sample Output
#
# 1
# 2
# Concept
#
# A tuple is similar to a list. However, a tuple is immutable. It cannot be changed. Once you assign some value to a tuple, it cannot be changed. Also, no additional members can be added once a tuple is assigned.
#
# For example:
# >> a = 1, # Define a tuple with one member
# >> a = (2, 6)
# >> a[1] = 1 # You cannot alter the elements in tuple.
# TypeError: 'tuple' object does not support item assignment
#
# For using a tuple, the method is similar to lists. Tuples are most commonly used to assign more than one variable in one statement, such as simultaneous assignment.
# */
#

# Enter your code here. Read input from STDIN. Print output to STDOUT
from __future__ import division

a = int(raw_input())
#b = int(raw_input())
#c = int(raw_input())
#d = int(raw_input())

for i in range(0,a):
    print i*i

