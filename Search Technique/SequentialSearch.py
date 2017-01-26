__author__ = 'Sanjay'


def seqSearch(aList, item):
    pos =0
    found = False

    while pos<len(aList) and not found:
        if aList[pos] == item:
            found = True
        else:
            pos = pos +1
    return found

#as per book
def sequentialSearch(alist, item):
    pos = 0
    found = False

    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos = pos+1

    return found

#sequential search for a ordered list.

    def orderedSequentialSearch(alist, item):
        pos = 0
        found = False
        stop = False
        while pos < len(alist) and not found and not stop:
            if alist[pos] == item:
                found = True
            else:
                if alist[pos] > item:
                    stop = True
                else:
                    pos = pos+1

            return found

	testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
	print(orderedSequentialSearch(testlist, 3))
	print(orderedSequentialSearch(testlist, 13))




if __name__ == '__main__':
    s= [1,2,32,42,12,4,3,45,454]
    print(seqSearch(s,45))

    testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]
    print(sequentialSearch(testlist, 3))
    print(sequentialSearch(testlist, 13))
