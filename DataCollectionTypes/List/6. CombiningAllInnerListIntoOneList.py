__author__ = 'Sanjay'

class singleList:
    def appendingAllElementsInAList(self, alist):
        finalOutput = []
        for i in alist:
            if type(i) == list:
                for z in i:
                    finalOutput.append(z)
            else:
                finalOutput.append(i)

        print("finally the output is..")
        print(finalOutput)


def genericSolutionUsingRecursive(inputList):
    pass

def genericSolutionWithoutUsingRecursive(inputList):
    outputArray = []
    for num in inputList:
        if type(num) == list:
            inputList.extend(num)
        else:
            outputArray.append(num)
    return outputArray


if __name__ == '__main__':

    firstInputList = ['a', 'b', 'c', 'd']

    firstInputList.append(list(range(1, 4)))                 # [1,2,3]
    print(firstInputList)                                    # ['a', 'b', 'c', 'd', [1, 2, 3]]

    ob = singleList()
    # ob.appendingAllElementsInAList(firstInputList)

    # Take this example, here elements inside the below lists are again list.
    sampleList = [[1, 2, 3], [4, 5, 6], [7], [8, 9]]
    flatList = []
    for listItem in sampleList:
        for item in listItem:
            flatList.append(item)

    # print(flatList)

    # hey the above code works only when all the elements inside the list, is also a type as list.
    # it wont work - sampleList = [[1, 2, 3], [4, 5, 6], [7], [8, 9], 10]
    # here's the solution.

    sampleListUC2 = [[1, 2, 3], [4, 5, 6], [7], [8, 9], 10]
    ob.appendingAllElementsInAList(sampleListUC2)

    ############## OTHER Best Solutions ##############

    # so from the above inputs, we understood, a list can have n number of arbitary items/list inside it.
    # what if the input is like [[1,2,3], [4,5,6], [[7,8,9], [10,[11,12, [13, 14, 15,]]]]]
    # we must have a generic function.

    sampleListUC3 = [[1,2,3], [4,5,6], [[7,8,9], [10,[11,12, [13, 14, 15,]]]]]
    answer = genericSolutionWithoutUsingRecursive(sampleListUC3)
    print(answer) # output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

    # here's the most fun code but only works when input is like [[1,2], [3,4], [5], [6]]
    # print(sum(sampleListUC2, []))




