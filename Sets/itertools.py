__author__ = 'Sanjay'

# a=map(int,raw_input().split(" "))
# b=map(int,raw_input().split(" "))
from itertools import product
a = [1,2]
b = [3,4]
s= tuple(product(a,b))
for i in list(product(a,b)):
    print i,