__author__ = 'Sanjay'

def compareTwoStrings(s1,s2):
    if s1 and s2 is not '':
        x = list(s1)
        y = list(s2)
        x.sort()
        y.sort()
        print (x,y)
        if s1 == s2:
            print("both strings are equal")
        else:
            print("its wrong")
    else:
        raise RuntimeError("something went bad")

if __name__ == '__main__':
    compareTwoStrings("abcde","edcba")
