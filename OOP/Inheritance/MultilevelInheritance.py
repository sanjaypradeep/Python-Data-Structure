# author = 'Sanjay'

class Father(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def behaviour(self):
        print ("I'm father! my behaviour is old.")


class FirstChild(Father):

    def __init__(self, a):
        self.a = a

    def behaviour(self):
        print ("I'm the child, but I feel responsible")


class SecondChild(FirstChild):
    def __init__(self):
        pass

    '''
    If method is uncommented, behaviour() will get call by its own class object.
    if the method is not available, then it will contact the inherited class.
    Even if the FirstChild class also doesn't have behaviour method, then it will contact
        Father class for sure and calls behaviour method.
    '''
    # def behaviour(self):
    #     print ("I have my own behaviour")

if __name__ == '__main__':
    c = SecondChild()
    c.behaviour()
    print (SecondChild.__mro__)