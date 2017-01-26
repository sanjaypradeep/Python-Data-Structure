
# Given an integer, , traverse its digits (1,2,...,n) and determine how many digits evenly divide  (i.e.: count the number of times  divided by each digit i has a remainder of ). Print the number of evenly divisible digits.

# Note: Each digit is considered to be unique, so each occurrence of the same evenly divisible digit should be counted (i.e.: for , the answer is ).

# Input Format

# The first line is an integer, , indicating the number of test cases.
# The  subsequent lines each contain an integer, .

# Output Format
# For every test case, count and print (on a new line) the number of digits in  that are able to evenly divide .

# Sample Input                              # Sample Output

# 2
# 12                                                2
# 1012                                              3

#Explanation:

# The number  is broken into two digits,  and . When  is divided by either of those digits, the calculation's remainder is ; thus, the number of evenly-divisible digits in  is .

# The number  is broken into four digits, , , , and .  is evenly divisible by its digits , , and , but it is not divisible by  as division by zero is undefined; thus, our count of evenly divisible digits is .

if __name__ =='__main__':

    t = int(input().strip())
    opToDisplay = []
    for a0 in range(t):
        n = int(input().strip())
        singleIterationResult = []
        splitResult = [int(i) for i in str(n)]
        for i in splitResult:
            if i != 0:
                if n % i == 0:
                    singleIterationResult.append(i)
        opToDisplay.append(len(singleIterationResult))
    for i in opToDisplay:
        print (i)
