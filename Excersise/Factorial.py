__author__ = 'Sanjay'

def fa(n):
    # if n==1:
    #     return 1
    # else:
    #     return fa(n) * fa(n-1)
    f = 1
    for i in range(n+1):
        if i is not 0:
            f = f*i
    print (f)


def fac(n):
    resp = 1
    givenInput = list(range(1, n+1))
    for i in givenInput:
        resp = resp * i

    return resp



if __name__ == '__main__':
    print ("Enter a number to find the factorial!")
    getInput = int(input())
    fa(getInput)
    fac(5)