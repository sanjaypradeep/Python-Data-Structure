__author__ = 'Sanjay'


def testingCustom(n):
    try:
        if n <0:
            # raise Exception('bad thing happened')
            raise SanjayException("bad thing happened")
        else:
            print ("number which you entered is", n)
    except SanjayException as e:
        SanjayException("Hey !! ")


class SanjayException(Exception):
    # def __init__(self,dErrorArguements):
    #     Exception.__init__(self,"my exception was raised with arguments {0}")
    #     self.dErrorArguments = dErrorArguements
    #
    # def __str__(self):
    #     return "sanjay"
    def __init__(self, argg):
        self.error = argg
        print(self.error)

if __name__ == '__main__':
    print ("inside main")
    testingCustom(-9)


