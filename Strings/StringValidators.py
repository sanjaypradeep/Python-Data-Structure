__author__ = 'Sanjay'
# Task
#
# You are given a string SS.
# Your task is to find out if the string SS contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.
#
# Input Format
#
# A single line containing a string SS.
#
# Constraints
#
# 0<len(S)<10000<len(S)<1000
# Output Format
#
# In the first line, print True if SS has any alphanumeric characters. Otherwise, print False.
# In the second line, print True if SS has any alphabetical characters. Otherwise, print False.
# In the third line, print True if SS has any digits. Otherwise, print False.
# In the fourth line, print True if SS has any lowercase characters. Otherwise, print False.
# In the fifth line, print True if SS has any uppercase characters. Otherwise, print False.
#
# Sample Input
#
# qA2
# Sample Output
#
# True
# True
# True
# True
# True
userGivenString = input()
l=list(userGivenString)
a,b,c,d,e=False,False,False,False,False
for i in l:
    if i.isalnum():
        a=True
    if i.isalpha():
        b=True
    if i.isdigit():
        c=True
    if i.islower():
        d=True
    if i.isupper():
        e=True
print (a)
print (b)
print (c)
print (d)
print (e)