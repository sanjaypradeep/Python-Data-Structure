from collections import Counter

# list1 = [1,2,2,2,4,4,4,4,4,4,4,4,'xyz', ['list1', 'list2'], {1:3, 2:4}]

def convertDict1(list1): #Method 1
    try:           
        print("Hello")
        myDict = {i:list1.count(i) for i in list1}
        return myDict
    except TypeError:
        print("Something went wrong!")

def convertDict2(list1): #Method 2
    myDict2 = dict(Counter(list1))
    return myDict2

def cleaningList1(list1):
    dummyList = []
    for i in list1:
        if type(i) == str or type(i) == int or isinstance(i, list):
            dummyList.append(i)
        else:
            pass
    return dummyList

if __name__ == "__main__":

    #list1 = list(input("Enter something here:"))
    list1 = [1,'xyz', ['list1', 'list2'], {1:3, 2:4}]

    firstLevel = cleaningList1(list1)
    print(convertDict1(firstLevel))
    
    # print(convertDict2(list1))
    # print(cleaningList1(list1))