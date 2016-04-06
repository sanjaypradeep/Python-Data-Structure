__author__ = 'Sanjay'
# Let's learn about Python's arithmetic operators.
#
# First, let's read two integers:
#
# a = int(raw_input())
# b = int(raw_input())
# The three basic arithmetic operators are the following:
#
# Addition (+)
# Subtraction (-)
# Multiplication (*)
# (We'll learn about division in the next task.)
#
# Task
# Read two integers from STDIN and print three lines where:
#
# The first line contains the sum of the two numbers.
# The second line contains the difference of the two numbers (first - second).
# The third line contains the product of the two numbers.
# Input Format
# The first line contains the first integer, aa. The second line contains the second integer, bb.
#
# Constraints
# 1?a?10101?a?1010
# 1?b?10101?b?1010
#
# Output Format
# Print the three lines as explained above.
#
# Sample Input
#
# 3
# 2
# Sample Output
#
# 5
# 1
# 6
# Explanation
# 3+2?53+2?5
# 3?2?13?2?1
# 3?2?6

# Enter your code here. Read input from STDIN. Print output to STDOUT
a = int(raw_input())
b = int(raw_input())

print a+b
print a-b
print a*b