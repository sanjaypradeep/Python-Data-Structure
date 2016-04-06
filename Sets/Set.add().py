__author__ = 'Sanjay'

#
# Task
#
# Apply your knowledge of the .add() operation to help your friend Rupal.
#
# Rupal has a huge collection of country stamps. She decided to count the total number of distinct country stamps in her collection. She asked for your help. You pick the stamps one by one from a stack of NN country stamps.
#
# Find the total number of distinct country stamps.
#
# Input Format
#
# The first line contains an integer NN, the total number of country stamps.
# The next NN lines contains the countrey's name where the stamp is from.
# Constraints
#
# 0<N<10000<N<1000
# Output Format
#
# Output the total number of distinct country stamps on a single line.
#
# Sample Input
#
# 7
# UK
# China
# USA
# France
# New Zealand
# UK
# France
# Sample Output
#
# 5

userInput1 = int(raw_input())
listOfCountries = []
for i in range(userInput1):
    #raw_input()
    listOfCountries.append(raw_input())
finalResult = set(listOfCountries)
print len(finalResult)
