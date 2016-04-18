__author__ = 'Sanjay'
#
# Input Format
#
#
# A single line of input containing the string S
# S
# .
#
# Constraints
#
# 3<len(S)<104
# 3<len(S)<104
#
#
# Output Format
#
#
# Print the three most common characters along with their occurrence count each on a separate line.
#  Sort output in descending order of occurrence count.
#  If the occurrence count is the same, sort the characters in ascending order.
#
#
# Sample Input
#
# aabbbccde
#
#
#
# Sample Output
#
# b 3
# a 2
# c 2
#
#
#
# Explanation
#
#
# Here, b occurs 3
# 3
#  times. It is printed first.
#  Both a and c occur 2
# 2
#  times. So, a is printed in the second line and c in the third line because a comes before c.
#
# Note: The string S
# S
#  has at least 3
# 3
#  distinct characters.

from collections import Counter
for k,v in sorted( Counter(raw_input()).most_common(3) , key = lambda x: (-x[1],x[0])):
         print k,v