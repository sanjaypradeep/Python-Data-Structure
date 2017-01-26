__author__ = 'Sanjay'

# Bob and Khatki recently started a business. They sell computers at moderate rates. To grow their business they need to know which company�s laptops are in demand. You are given description of N laptops which are sold out. Each laptop is described by their company name. Can you help them figure out which company�s laptops are in demand. The company in demand is the one whose laptops are being sold more. If there are multiple such companies print the one which is lexicographically smallest.
#
# Input:
#
# First line of input contains N, number of responses of people. Next N lines contains company name of laptop.
#
# Output:
#
# Print the company name people preferred most. In case of tie print the lexographically smallest answer.
#
# Constraints:
#
# 1 &le N ? 105

# SAMPLE INPUT

#9
# dell
# lenovo
# hp
# lenovo
# dell
# dell
# apple
# compaq
# sony
#

# SAMPLE OUTPUT
# dell


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
            print (i)



if __name__ == "__main__":
    userResponseCount = input()
    userInputList = []
    for i in range(0,userResponseCount):
        temp = input()
        userInputList.append(temp)
    mostTrendingBrand(userResponseCount,userInputList)
