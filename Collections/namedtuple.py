__author__ = 'Sanjay'
#
# Task
#
# Dr. John Wesley has a spreadsheet containing a list of student's IDs
# IDs
# , marks
# marks
# , class
# class
#  and name
# name
# .
#
# Your task is to help Dr. Wesley calculate the average marks of the students.
#
#
# Average=Sum of all marksTotal Students
# Average=Sum of all marksTotal Students
#
# Note:
#  1. Columns can be in any order. IDs, marks, class and name can be written in any order in the spreadsheet.
#  2. Column names are ID, MARKS, CLASS and NAME. (The spelling and case type of these names won't change.)
#
#
# Input Format
#
#
# The first line contains an integer N
# N
# , the total number of students.
#  The second line contains the names of the columns in any order.
#  The next N
# N
#  lines contains the marks
# marks
# , IDs
# IDs
# , name
# name
#  and class
# class
# , under their respective column names.
#
# Constraints
#
# 0<N?100
# 0<N?100
#
#
# Output Format
#
#
# Print the average marks of the list corrected to 2 decimal places.
#
#
# Sample Input
#
#
# TESTCASE 01
# 5
# ID         MARKS      NAME       CLASS
# 1          97         Raymond    7
# 2          50         Steven     4
# 3          91         Adrian     9
# 4          72         Stewart    5
# 5          80         Peter      6
#
#
# TESTCASE 02
# 5
# MARKS      CLASS      NAME       ID
# 92         2          Calum      1
# 82         5          Scott      2
# 94         2          Jason      3
# 55         8          Glenn      4
# 82         2          Fergus     5
#
#
#
# Sample Output
#
#
# TESTCASE 01
# 78.00
#
#
# TESTCASE 02
# 81.00
#
#
#
# Explanation
#
#
# TESTCASE 01
#
# Average = (97+50+91+72+80)/5
# (97+50+91+72+80)/5
#
# Can you solve this challenge in 4 lines of code or less?
# NOTE: There is no penalty for solutions that are correct but have more than 4 lines.

stu, marks = int(input()), input().split().index("MARKS")
print (sum([int(input().split()[marks]) for _ in range(stu)]) / stu)