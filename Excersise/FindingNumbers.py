# Alice has just learnt multiplying two integers. He wants to multiply two integers X and Y to form a number Z. To make the problem interesting he will choose X in the range [1,M] and Y in the range [1,N]. Help him to find the number of ways in which he can do this.
#
# Input
# First line of the input is the number of test cases T. It is followed by T lines. Each line has three space separated integers, the numbers Z, M and N.
#
# Output
# For each test case output a single integer, the number of ways.
#
# Constraints
# 1 <= T <= 50
# 1 <= Z <= 10^12
# 1 <= M <= 10^12
# 1 <= N <= 10^12

# SAMPLE INPUT            SAMPLE OUTPUT
# 4
# 4 7 9                       3
# 5 2 10                      1
# 5 5 6                       2
# 2 8 1                       1


def findNumbers(totalTest):
    for i in range(totalTestCases):
        del finalOp[:]
        count = 0
        resultSum, firstInput, secondInput = map(int,input().split())
        firstList = range(1, firstInput+1)
        secondList = range(1, secondInput+1)
        if not firstList or not secondList:
            finalOp.append(1)
        else:
            for i in firstList:
                for j in secondList:
                    if i*j == resultSum or j*i == resultSum:
                        count = count + 1
                        finalOp.append(1)
                    else:
                        pass
       # print len(finalOp)
        print (count)

# def secondD+ayTry(totalTestC):
#     op = []
#     res = 0
#     for i in range(totalTestC):
#         resultSum, firstInput, secondInput = map(int, raw_input().split())
#         firstList = range(1, firstInput)
#         secondList = range(1, secondInput)
#
#         if not firstList or not secondList:
#           op.append(1)
#         else:
#             for m in firstList:
#                 op.append(res)
#                 res = 0
#                 for n in secondList:
#                       if m*n == resultSum:
#                           res = res +1
#
#             print res
#
#     for i in op:
#         print "result is",i



if __name__ == '__main__':
    totalTestCases = int(input())
    finalOp = []
    findNumbers(totalTestCases)