__author__ = 'Sanjay'

# Task
# Given 22 sets of integers, MM and NN, print their symmetric difference in ascending order. The term symmetric difference indicates those values that exist in either MM or NN but do not exist in both.
#
# Input Format
#
# The first line of input contains an integer, MM.
# The second line contains MM space-separated integers.
# The third line contains an integer, NN.
# The fourth line contains NN space-separated integers.
#
# Output Format
#
# Output the symmetric difference integers in ascending order, one per line.
#
# Sample Input
#
# 4
# 2 4 5 9
# 4
# 2 4 11 12
# Sample Output
#
# 5
# 9
# 11
# 12

input()
a=set(map(int,raw_input().split()))
input()
b=set(map(int,raw_input().split()))
c=a.symmetric_difference(b)
for n in sorted(list(c)):
    print n