# https://www.hackerrank.com/challenges/plus-minus


totalElements = int(input())
giveInputList = list(map(int, input().split()))

print(totalElements, len(giveInputList))
if totalElements == len(giveInputList):
    positiveElements = [i for i in giveInputList if i>0]
    negativeElements = [i for i in giveInputList if i<0]
    neutralElements = [i for i in giveInputList if i ==0]

    print (round(len(positiveElements)/totalElements , 6))
    print (round(len(negativeElements)/ totalElements, 6))
    print (round(len(neutralElements)/ totalElements, 6))


