# https://www.hackerrank.com/challenges/staircase?h_r=next-challenge&h_v=zen


totalNumberSteps = int(input())
space = " "

# totalSpaceNeeded = space * totalNumberSteps
# print (totalSpaceNeeded)
for i in range(1, totalNumberSteps+1):
    print(space*(totalNumberSteps-i)+ '#'*i )