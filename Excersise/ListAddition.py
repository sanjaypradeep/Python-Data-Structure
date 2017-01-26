__author__ = 'Sanjay'

# Question
# There are 2 arrays of integers.You have to add the those integers and keep it in 3rd array.there is one condition, if the sum is a 2 digit number, split that number into single digiit and other condition is if any of the array integer is left then print that number
# I/P:
# int[] a = {1,2,3,4,5,6}
# int[] b = {2,3,4,5,6,7,8}
# o/p:
# {3,5,7,9,1,1,1,3,8}

def ListAdditionOutputWithCommaSeparated(a,b):
    try:
        s= ""
        for i in range(len(a)):
            c = a[i] + b[i]
            s = s + str(c)
        print ([int(i) for i in s])
    except (IndexError, ValueError):
        print (ValueError)


def genericCheck(a,b):
    diff = len(a) - len(b)
    for i in range(diff):
        b.append(0)
    ListAdditionOutputWithCommaSeparated(a,b)

if __name__ == '__main__':
    a = range(10)
    b = range(11,21)
    if len(a) > len(b):
        genericCheck(a,b)
    elif(len(b) > len(a)):
        genericCheck(a,b)
    else:
        ListAdditionOutputWithCommaSeparated(a,b)