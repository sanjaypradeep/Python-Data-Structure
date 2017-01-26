__author__ = 'Sanjay'

class Fraction:

    def __init__(self,top,bottom):

        self.num = top
        self.den = bottom

    def display(self):
        print("here are the input numbers")
        print (self.num,  "/", self.den)

    def division(self):
        c = self.num / self.den
        if c is not 0:
            print ("the value of c is ",c)
        else:
            print ("it seems it's zero")

    def __add__(self, other):
        newnum = self.num * other.den + self.den * other.num
        newden = self.den * other.den

        return Fraction(newnum, newden)
#
# object.__add__(self, other)
# object.__sub__(self, other)
# object.__mul__(self, other)
# object.__floordiv__(self, other)
# object.__mod__(self, other)
# object.__divmod__(self, other)
# object.__pow__(self, other[, modulo])
# object.__lshift__(self, other)
# object.__rshift__(self, other)
# object.__and__(self, other)
# object.__xor__(self, other)
# object.__or__(self, other)


if __name__ == '__main__':
    myFrac = Fraction(3,5)
    print (myFrac)
    myFrac.display()
    myFrac.division()
    f1 = Fraction(1,4)
    f2 = Fraction(1,2)
    f3 = f1+f2
    print (f3)

