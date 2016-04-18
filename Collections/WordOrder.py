__author__ = 'Sanjay'

#
# Input Format
#
#
# The first line contains the integer, n
# n
# .
#  The next n
# n
#  lines each contain a word.
#
#
# Output Format
#
#
# Output 2
# 2
#  lines.
#  On the first line, output the number of distinct words from the input.
#  On the second line, output the number of occurrences for each distinct word according to their appearance in the input.
#
#
# Sample Input
#
# 4
# bcdef
# abcdefg
# bcde
# bcdef
#
#
#
# Sample Output
#
# 3
# 2 1 1
#
#
#
# Explanation
#
#
# There are 3
# 3
#  distinct words. Here, "bcdef" appears twice in the input at the first and last positions. The other words appear once each. The order of the first appearances are "bcdef", "abcdefg" and "bcde" which corresponds to the output.

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

n = int(raw_input())
words = [raw_input().strip() for _ in range(n)]
counts = Counter(words)

print len(counts)

for word in words:
    derp = counts.pop(word, None)
    if derp == None:
        continue
    else:
        print derp, # comma stops print from ending with newline