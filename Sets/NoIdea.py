# There is an array of nn integers. There are also 22 disjoint sets, AA and BB, each containing mm integers. You like all the integers in set AA and dislike all the integers in set BB. Your initial happiness is 00. For each ii integer in the array, if i?Ai?A, you add 11 to your happiness. If i?Bi?B, you add ?1?1 to your happiness. Otherwise, your happiness does not change. Output your final happiness at the end.
#
# Note: Since AA and BB are sets, they have no repeated elements. However, the array might contain duplicate elements.
#
# Constraints
# 1?n?1051?n?105
# 1?m?1051?m?105
# 1?Any integer in the input?1091?Any integer in the input?109
#
# Input Format
#
# The first line contains integers nn and mm separated by a space.
# The second line contains nn integers, the elements of the array.
# The third and fourth lines contain mm integers, AA and BB, respectively.
#
# Output Format
#
# Output a single integer, your total happiness.
#
# Sample Input
#
# 3 2
# 1 5 3
# 3 1
# 5 7
# Sample Output
#
# 1
# Explanation
#
# You gain 11 unit of happiness for elements 33 and 11 in set AA. You lose 11 unit for 55 in set BB. The element 77 in set BB does not exist in the array so it is not included in the calculation.
#
# Hence, the total happiness is 2?1=12?1=1.

# Enter your code here. Read input from STDIN. Print output to STDOUT
a= raw_input() == "" or list(map(int, raw_input().split()))
b = set(map(int, raw_input().split()))
c = set(map(int, raw_input().split()))
print sum([1 if x in b else 0 for x in a]) - sum([1 if x in c else 0 for x in a])