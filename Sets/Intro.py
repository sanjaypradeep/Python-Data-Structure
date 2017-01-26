__author__ = 'Sanjay'
#
# Input Format
#
# The first line contains the integer, NN, the total number of plants.
# The second line contains the NN space separated heights of the plants.
#
# Constraints
#
# 0<N?1000<N?100
# Output Format
#
# Output the average height value on a single line.
#
# Sample Input
#
# 10
# 161 182 161 154 176 170 167 171 170 174
# Sample Output
#
# 169.375
input()
s=set(map(int,input().split()))
print(sum(s)/float(len(s)))
