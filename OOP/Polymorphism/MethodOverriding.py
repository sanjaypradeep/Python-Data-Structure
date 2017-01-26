
class A(object):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def m1(self):
        print "inside A"

class B(A):

    def __init__(self):
        print ("b constructor")
    # def m1(self):
    #     print "inside b"

bb = B()
bb.m1()