__author__ = 'Sanjay'

# Input Format

# The first line contains an integer, NN, the number of students.
# The 2N2N subsequent lines describe each student over 22 lines; the first line contains a student's name, and the second line contains their grade.

# Constraints
#
# 2?N?52?N?5
# There will always be one or more students having the second lowest grade.
# Output Format

# Print the name(s) of any student(s) having the second lowest grade in Physics; if there are multiple students, order their names alphabetically and print each one on a new line.

# Sample Input

# 5
# Harry
# 37.21
# Berry
# 37.21
# Tina
# 37.2
# Akriti
# 41
# Harsh
# 39
# Sample Output

# Berry
# Harry
# Explanation

# There are 55 students in this class whose names and grades are assembled to build the following list:

# students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
# The lowest grade of 37.237.2 belongs to Tina. The second lowest grade of 37.2137.21 belongs to both Harry and Berry,
# so we order their names alphabetically and print each name on a new line.

n = int(input())
marks = [[input(), float(input())] for i in  range(n)]
scores = sorted({s[1] for s in marks})
result = sorted(s[0] for s in marks if s[1] == scores[1])
print ('\n'.join(result))

#ends