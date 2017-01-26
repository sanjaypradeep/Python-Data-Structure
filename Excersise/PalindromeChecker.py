__author__ = 'Sanjay'

from Queue import Deque
def palin(inputString):

    try:
        rValue = inputString[::-1]

        if (inputString == rValue):
            print ("It's a palindrome")
        else:
            print ("it's not a palidrome")
    except IndexError as e:
        print (e)
    else:
        print ("all is well..")

if __name__ == '__main__':
    palin('madam')

# book method

def palchecker(aString):
    chardeque = Deque()

    for ch in aString:
        chardeque.addRear(ch)

    stillEqual = True

    while chardeque.size() > 1 and stillEqual:
        first = chardeque.removeFront()
        last = chardeque.removeRear()
        if first != last:
            stillEqual = False

    return stillEqual

