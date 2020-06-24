# author = _'Sanjay'

class SampleClass(object):

    # for name sake, I've defined a default constructor.
    def __init__(self):
        pass
        
    def add(self, firstNum, secondNum):
        '''
        @name: add
        @param: firstNum, secondNum
        @desc: Takes two input paramter, adding them and returning
        @return: sum(firstNum, secondNum)
        '''
        return self.firstNum + self.secondNum

    
    # this method does the same as above, but the difference is, it takes 3 parameter here.
    def add(self, firstNum, secondNum, thirdNum):
        '''
        @name : add
        @param: firstNum, secondNum, thirdNum
        @desc: takes three input parameter, adding them and returning
        @return : sum(firstNum, secondNum, threeNum)
        '''
        return self.firstNum + self.secondNum + self.thirdNum

#Method overloading is not possible
# This is compile time polymorphism. 
x = SampleClass()
x.add(1,2,3)
