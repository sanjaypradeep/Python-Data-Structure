__author__ = 'Sanjay'
#
# Task
#
#
# The students of District College have subscriptions to English and French newspapers. Some students have subscribed only to English, some have subscribed only to French, and some have subscribed to both newspapers.
#
# You are given two sets of student roll numbers. One set has subscribed to the English newspaper, one set has subscribed to the French newspaper. Your task is to find the total number of students who have subscribed to both newspapers.
#
#
# Input Format
#
#
# The first line contains n
# n
# , the number of students who have subscribed to the English newspaper.
#  The second line contains n
# n
#  space separated roll numbers of those students.
#  The third line contains b
# b
# , the number of students who have subscribed to the French newspaper.
#  The fourth line contains b
# b
#  space separated roll numbers of those students.
#
# Constraints
#
# 0<Total number of students in college<1000
# 0<Total number of students in college<1000
#
#
# Output Format
#
#
# Output the total number of students who have subscriptions to both English and French newspapers.
#
#
# Sample Input
#
# 9
# 1 2 3 4 5 6 7 8 9
# 9
# 10 1 2 3 11 21 55 6 8
#
#
#
# Sample Output
#
# 5
#

#print ((len(input()==0 or set(input().split()) & (input()==0 or set(input().split())))))
raw_input()
t=set(map(int,raw_input().split()))
raw_input()
print len(t.intersection(set(map(int,raw_input().split()))))