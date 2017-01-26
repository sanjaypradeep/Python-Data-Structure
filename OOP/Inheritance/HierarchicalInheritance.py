# author = 'Sanjay'


class Father(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def myCharacter(self):
        print ("Lets help as much as we can!")

    def myBehaviour(self):
        print ("Old is gold!")


class FirstChild(Father):

    def __init__(self,a):
        self.a = a

    def myCharacter(self):
        print ("I'm the first child, I'll get angry at times.")


class SecondChild(Father):  # Method resolution order
    def __init__(self):
        print("My father is all to me!")


if __name__ == '__main__':
    secondObj = SecondChild()
    secondObj.myCharacter()
    secondObj.myBehaviour()

    firstChildObj = FirstChild(10)
    firstChildObj.myCharacter()
    firstChildObj.myBehaviour() #firstchild doesn't contain myBehaviour method, so it has to contact base myBehaviour only.

