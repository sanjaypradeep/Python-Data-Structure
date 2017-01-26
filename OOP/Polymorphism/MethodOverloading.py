# author = _'Sanjay'

class A(object):

    def __init__(self):
        pass

    def add(self, a, b):
        print self.a + self.b

    def add(self, a, b, c):
        print a + b + c

#Method overloading is not possible
# This is compile time polymorphism. 
x = A()
x.add(1,2,3)
