__author__ = 'Sanjay'
from itertools import *

#
# Task
#
# You are given a two lists A
# A and B
# Your task is to compute their cartesian product A
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
# B are sorted lists, and the cartesian product's tuples should be output in sorted order.

# Input Format

# The first line contains the space separated elements of list A
# A
# .
#  The second line contains the space separated elements of list B
# B
# .
# Both lists have no duplicate integer elements.
# Constraints
# 0<A<30
# 0<A<30
# 0<B<30
# 0<B<30

# Output Format
# Output the space separated tuples of the cartesian product.
# Sample Input


#  1 2
#  3 4

# Sample Output
#  (1, 3) (1, 4) (2, 3) (2, 4)

firstInput = list(map(int, input().split()))
secondInput = list(map(int, input().split()))

for i in list(product(firstInput, secondInput)):
    print(i, end="")


# list1 = [1,2,3,4]
# list2 = ['Hello', 'world']

# opList= []
# if len(list1) > len(list2):
#     for i in list(range(0, len(list2))):        
#         print(str(list1[i]) + list2[i])
#         opList.append(str(list1[i]) + list2[i])

#     diff = (len(list1) - len(list2) - 1)
#     for i in list1[diff:]:
#         opList.append(list1[i])

#     print(opList)



# op = [(1, 'Hello'), (2, 'World'), (3, None), (4, None)]
# op_2 = [(None, 'Hello'), (None, 'World'), (1, 'Hello'), (2, 'World')]

# finalOp = []

# for i in op:    
#     firstEle = "" if i[0] == None else i[0]
#     secEle = "" if i[1] == None else i[1]
#     finalOp.append(str(firstEle) + secEle)

# print(finalOp)
    