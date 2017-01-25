__author__ = 'Sanjay'

# This below excercise is given in HackersEarth Practice.

def monk(n, args = []):

    someArray = range(0,50,10)
    for i in args:
        if i in someArray:
            print ("YES")
        else:
            print ("NO")

if __name__ == '__main__':
    someList = range(0,100,10)
    monk(len(someList), someList)

