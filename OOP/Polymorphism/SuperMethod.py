class SomeBaseClass(object):
    def __init__(self):
        print('SomeBaseClass.__init__(self) called')

class UnsuperChild(SomeBaseClass):
    def __init__(self):
        print('Child.__init__(self) called')
        SomeBaseClass.__init__(self)

class SuperChild(SomeBaseClass):
    def __init__(self):
        print('SuperChild.__init__(self) called')
        super(SuperChild, self).__init__()

s = SuperChild()

print s
u = UnsuperChild()
# print "**"
print u
# print "****"

class InjectMe(SomeBaseClass):
    def __init__(self):
        print('InjectMe.__init__(self) called')
        super(InjectMe, self).__init__()

class UnsuperInjector(UnsuperChild, InjectMe): pass

class SuperInjector(SuperChild, InjectMe): pass

print "-----------------"
x = SuperInjector()
#x.mro

y = UnsuperInjector()

print "MRO.."
print SuperInjector.mro()
print UnsuperInjector.mro()