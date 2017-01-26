__author__ = 'Sanjay'

# Let's delve into one of the most basic data types in Python, the list. You are given NN numbers. Store them in a list and find the second largest number.
#
# Input Format
#
# The first line contains NN. The second line contains an array AA[] of NN integers each separated by a space.
#
# Output Format
#
# Output the value of the second largest number.
#
# Sample Input
#
# 5
# 2 3 6 6 5
# Sample Output
#
# 5
# Constraints
# 2?N?102?N?10
# ?100?A[i]?100?100?A[i]?100
# Concept
#
# A list in Python is similar to an array. A list can contain any data type as well as mixed data types. A list can contain a number, a string and even another list.
# Lists are mutable. They can be changed by adding or removing values from the list.

input()
a=list(map(int,input().split(" ")))
b=max(a)
while max(a)==b :
    a.remove(b)
print (max(a))