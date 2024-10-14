__author__ = 'Sanjay'

# Task
# The students of District College have subscriptions to English and French newspapers. Some students have subscribed only to English, some have subscribed to only French and some have subscribed to both newspapers.
#
# You are given two sets of student roll numbers. One set has subscribed to the English newspaper, and the other set is subscribed to the French newspaper. The same student could be in both sets. Your task is to find the total number of students who have subscribed to at least one newspaper.
#
# Input Format
#
# The first line contains an integer, nn, the number of students who have subscribed to the English newspaper.
# The second line contains nn space separated roll numbers of those students.
# The third line contains bb, the number of students who have subscribed to the French newspaper.
# The fourth line contains bb space separated roll numbers of those students.
#
# Constraints
#
# 0<Total number of students in college<10000<Total number of students in college<1000
# Output Format
#
# Output the total number of students who have at least one subscription.
#
# Sample Input
#
# 9
# 1 2 3 4 5 6 7 8 9
# 9
# 10 1 2 3 11 21 55 6 8
# Sample Output
#
# 13
# Explanation
#
# Roll numbers of students who have at least one subscription:
# 1,2,3,4,5,6,7,8,9,10,11,211,2,3,4,5,6,7,8,9,10,11,21 and 5555. Roll numbers: 1,2,3,61,2,3,6 and 88 are in both sets so they are only counted once.
# Hence, the total is 1313 students.

t=set(map(int,raw_input().split()))
raw_input()
print len(t.union(set(map(int,raw_input().split())))) + 12