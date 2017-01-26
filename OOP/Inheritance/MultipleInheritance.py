# author = 'Sanjay'

'''
We have two classes here,
    1. Father - Parent Independent Class
    2. Mother - Parent Independent Class
    3. ChildClass - Inherits Father and Mother

Questions:
    1. ChildClass will always get confused whom to listen and whom not to ignore.
    2. Because, child inherits both the parent class
    3. How can we solve this? Whenever there's a action needed,
        child should either react for father or another father instructions.
        Child has to give priority to what to listen and what not to.

OK! We have something called, ****Method Resolution Order*****
Decision on what parent to listen is happening here!

Scenario 1:
class ChildClass(Mother, Father): #consider child class dont have getUpEarlyMorninig method

    When we create a Object for the ChildClass and call the getUpEarlyMorning,
    which parent would be called here. To check that, we can find that via __mro__


objectForChildClass = ChildClass()
objectForChildClass.__mro__()

Output:
(<class '__main__.ChildClass'>, <class '__main__.Mother'>, <class '__main__.Father'>, <type 'object'>)

Scenario 2:
class ChildClass(Mother, Father):
    pass

objectForChildClass = ChildClass()
objectForChildClass.__mro__()

Output:
(<class '__main__.ChildClass'>, <class '__main__.Father'>, <class '__main__.Mother'>, <type 'object'>)

Scenario 3:
Considering ChildClass has a getUpEarlyMorning method

if Child has decided when to wake up on its own, it don't need to listen parents for sure. They have their own thoughts to
folllow.

Output:I will get up at 5 AM

'''


class Father(object):
    def __init__(self):
        pass

    def getUpEarlyMorning(self):
        print("Get up Early at 6 AM")


class Mother(object): # please don't mind the name of the class

    def __init__(self):
        pass

    def getUpEarlyMorning(self):
        print("Get up Early at 4 AM")


class ChildClass(Mother, Father):  # Method resolution order
    # Child is ready to listen both Mother and Father behaviour, but priority goes to mom first.
    # Because, we are inheriting "Mother" first. (Method Resolution Order)
    def __init__(self):
        pass

    def getUpEarlyMorning(self):
        print("I will get up at 5 AM")
        # pass

if __name__ == '__main__':
    b = ChildClass()
    b.getUpEarlyMorning()
    print (ChildClass.__mro__)