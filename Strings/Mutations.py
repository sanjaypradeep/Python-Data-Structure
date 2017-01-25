__author__ = 'Sanjay'

# Task
# Read a given string, change the character at a given index and then print the modified string.
#
# Input Format
# The first line contains a string, SS.
# The next line contains an integer ii, denoting the index location and a character cc separated by a space.
#
# Output Format
# Using any of the methods explained above, replace the character at index ii with character cc.
#
# Sample Input
#
# abracadabra
# 5 k
# Sample Output
#
# abrackdabra


userInput = input()
index, stringTobeReplaced = input().split(" ")

l = list(userInput)
l[int(index)] = stringTobeReplaced
userInput = ''.join(l)
print (userInput)

