'''
Given a list of N numbers, use a single list comprehension to produce a new list that only contains those values that are:
(a) even numbers, and
(b) from elements in the original list that had even indices
For example, if list[2] contains a value that is even, that value should be included in the new list, 
since it is also at an even index (i.e., 2) in the original list. 
However, if list[3] contains an even number, that number should not be included in the new list since 
it is at an odd index (i.e., 3) in the original list. 
'''

def EvenNumEvenIndex(someList):
    if type(someList) is not list:
        print("Invalid user input")
    if len(someList) == 0:
        print("No value in the list")

    dummyList = []
    for num in someList:
        if someList.index(num) %2 == 0 and num %2 == 0:
            dummyList.append(int(num))
    return dummyList


def getUserInput():
    listOfIntNum = []
    listOfFloatNum = []

    inputList = input("Enter list of nunmbers: ")
    inputList = inputList.split(" ")

    if inputList:
        for value in inputList:            
            if '.' in value:
                # possible that, value can be a floating number or a sentence with full stop.
                try:
                    if isinstance(float(value), float):
                        listOfFloatNum.append(float(value))
                        continue
                except ValueError as e:
                    pass
            try:
                if isinstance(int(value), int):
                    listOfIntNum.append(int(value))
            except ValueError as e:
                pass


    return listOfIntNum + listOfFloatNum

if __name__ == "__main__":
    numList = getUserInput()
    print(numList)
    print(EvenNumEvenIndex(numList)) 