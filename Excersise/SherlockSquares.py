# Fromm HackerEarth
# Watson gives two integers ( and ) to Sherlock and asks if he can count the number of square integers between  and  (both inclusive).
#
# Note: A square integer is an integer which is the square of any integer. For example, 1, 4, 9, and 16 are some of the square integers as they are squares of 1, 2, 3, and 4, respectively.
#
# Input Format
# The first line contains , the number of test cases.  test cases follow, each in a new line.
# Each test case contains two space-separated integers denoting  and .
#
# Output Format
# For each test case, print the required answer in a new line.
#
# Constraints
# 1<=T<=100
# 1<=A<=B<=10^9
#
# Sample Input			Sample output
# 2
# 3 9						2
# 17 24						0

if __name__ == '__main__':
    squares = [i*i for i in range(1, 1000000001)]
    print (squares)
    print (len(squares))
    iterationResult = []
    # listOfPossibleSquares = []
    testCases = int(input().strip())
    for i in range(testCases):
        listOfPossibleSquares = []
        fromValue, toValue = map(int, input().split())
        for k in range(fromValue,(toValue+1)):
            if k in squares:
                listOfPossibleSquares.append(k)
        iterationResult.append(len(listOfPossibleSquares))
    for i in iterationResult:
        print (i)