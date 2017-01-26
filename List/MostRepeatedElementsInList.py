__author__ = 'Sanjay'
from collections import Counter
import operator

def mostTrendingBrand(numOfResponse,listOfBrands):
    if numOfResponse>1:
        brandCount = Counter(listOfBrands)
        onlyCount = []
        for ke,va in brandCount.iteritems():
            onlyCount.append(va)
        trendingCount = max(onlyCount)
        trendingBrandOutput = []
        for ke,va in brandCount.iteritems():
            if trendingCount == va:
                trendingBrandOutput.append(ke)
        for i in trendingBrandOutput:
            print "Most repeated item is",i



if __name__ == "__main__":
    x = input()
    userInputList = []
    for i in range(0,x):
        temp = raw_input()
        userInputList.append(temp)
    mostTrendingBrand(x,userInputList)


# Sample output
# 5
# 'a'
# 'b'
# 'a'
# 'a'
# 'b'

# Most repeated item is 'a'
