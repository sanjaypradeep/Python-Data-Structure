# Author = __Sanjay

from __future__ import division
def isDivide(x,y):
    try:
        if x >= 1:
            if x > y:
                print (abs(x/y))
            elif y > x:
                print (abs(y/x))
            else:
                raise ZeroDivisionError
    except ZeroDivisionError as e:
        print (e)
    else:
        print ("inside else")
    finally:
        print ("inside finally")
        # raise ZeroDivisionError

if __name__ == '__main__':
    # isDivide(1, 10)
    isDivide(10, 0)