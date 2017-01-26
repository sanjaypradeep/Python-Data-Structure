__author__ = 'Sanjay'


def testingCustom(n):
    if n <0:
        raise SanjayException("hey")
    else:
        print "number which you entered is", n


class SanjayException(Exception):
    def __init__(self,dErrorArguements):
        Exception.__init__(self,"my exception was raised with arguments {0}")
        self.dErrorArguments = dErrorArguements

    def __str__(self):
        return "sanjay"


if __name__ == '__main__':
    print "inside main"
    testingCustom(-9)


