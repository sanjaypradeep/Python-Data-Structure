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


if __name__ == '__main__':

    firstInputList = ['a', 'b', 'c', 'd']
    secondInputList = list(range(1, 4)) # [1,2,3]
    firstInputList.append(secondInputList)
    print(firstInputList)  # ['a', 'b', 'c', 'd', [1, 2, 3]]
    ob = singleList()
    ob.appendingAllElementsInAList(firstInputList)

    # Take this example, here elements inside the below lists are again list.
    sampleList = [[1, 2, 3], [4, 5, 6], [7], [8, 9]]
    flatList = []
    for listItem in sampleList:
        for item in listItem:
            flatList.append(item)

    print(flatList)

    # hey the above code works only when all the elements inside the list, is also a type as list.
    # it wont work - sampleList = [[1, 2, 3], [4, 5, 6], [7], [8, 9], 10]
    # here's the solution.
    sampleListUC2 = [[1, 2, 3], [4, 5, 6], [7], [8, 9], 10]
    ob.appendingAllElementsInAList(sampleListUC2)




    # here's the most fun code
    print(sum(sampleList, []))




