__author__ = 'Sanjay'
from collections import Counter
import operator

# TODO: Below commented code must  be cleaned or refactored, after understanding the usage of this logic.
# def mostTrendingBrand(numOfResponse, listOfBrands):
#     if numOfResponse>1:
#         brandCount = Counter(listOfBrands)
#         onlyCount = []
#         for ke,va in brandCount.iteritems():
#             onlyCount.append(va)
#         trendingCount = max(onlyCount)
#         trendingBrandOutput = []
#         for ke,va in brandCount.iteritems():
#             if trendingCount == va:
#                 trendingBrandOutput.append(ke)
#         for i in trendingBrandOutput:
#             print("Most repeated item is",i)


# current this function takes input as a list, to find maximum repeated elements in the list. 
def mostTrendingBrancAlternateSolution(userInputs):
    finalOp = {}
    for element in userInputs:
        finalOp[element] = userInputs.count(element)
    print(finalOp)
    for key, value in finalOp.items():
        if value == max(list(finalOp.values())):
            print("Maximum repeated brand is ", key)

if __name__ == "__main__":
    x = int(input())
    userInputList = []
    for i in range(0, x):
        temp = input()
        userInputList.append(temp)
    # mostTrendingBrand(x, userInputList)
    mostTrendingBrancAlternateSolution(userInputList)


# Sample output
# 5
# 'a'
# 'b'
# 'a'
# 'a'
# 'b'

# Most repeated item is 'a'
