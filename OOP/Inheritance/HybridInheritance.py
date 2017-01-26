# author = 'Sanjay'


class GrandFather(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def myCharacter(self):
        print ("Lets help as much as we can!")

    def myBehaviour(self):
        print ("Old is gold!")


class Father(GrandFather):

    def __init__(self):
        pass

    def myCharacter(self):
        print ("I have my own Character! I'm a father of two child")


class FirstChild(Father):
    def __init__(self):
        pass

    def myCharacter(self):
        print ("I have my own character, May be because I behave like my dad.")


class SecondChild(Father):
    def __init__(self):
        print ("I dont need to be unique, My Father is already having good character and my grand father is having good"
               "behaviour")

if __name__ == '__main__':
    firstChildObj = FirstChild()
    firstChildObj.myCharacter()
    firstChildObj.myBehaviour()
    # firstchild doesn't contain myBehaviour method,
    # it contacts father and search for myBehaviour, father also doesn't have
    # o it has to contact base myBehaviour only.

    secondChildObj = SecondChild()
    secondChildObj.myCharacter()
    secondChildObj.myBehaviour()



