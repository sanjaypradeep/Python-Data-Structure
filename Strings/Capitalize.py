__author__ = 'Sanjay'

# You are given a string SS. Your task is to capitalize each word of SS.
#
# Input Format
#
# A single line of input containing the string, SS.
#
# Constraints
#
# 0<len(S)<10000<len(S)<1000
# The string consists of alphanumeric characters and spaces.
#
# Output Format
#
# Print the capitalized string, SS.
#
# Sample Input
#
# hello world
# Sample Output
#
# Hello World

userInput = raw_input()

l = userInput.split(" ")

for i in l:
    print i.capitalize(),