
def __onlyCommonEle(p):
    if len(p) == 0:
        return
    print(set(p[0]).intersection(*p))    

def findCommonElements(*args):
    if len(args) == 0:
        return
    __onlyCommonEle([i for i in args if type(i) == list])
    

findCommonElements([1,2,3], 'a', 'c', ['a','b',1,2,4])