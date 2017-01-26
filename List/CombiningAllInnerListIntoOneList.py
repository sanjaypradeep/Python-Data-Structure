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

        print "finally the output is.."
        print finalOutput

if __name__ == '__main__':

    firstInputList = ['a', 'b', 'c', 'd']
    secondInputList = range(1, 4)  # [1,2,3]
    firstInputList.append(secondInputList)
    print firstInputList  # ['a', 'b', 'c', 'd', [1, 2, 3]]
    ob = singleList()
    ob.appendingAllElementsInAList(firstInputList)

