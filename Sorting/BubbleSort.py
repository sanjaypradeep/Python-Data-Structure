__author__ = 'Sanjay'

def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

if __name__ == '__main__':
    alist = [54,26,93,17,77,31,44,55,20]
    bubbleSort(alist)
    print(alist)