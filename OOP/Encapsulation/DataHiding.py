# Encapsulation is nothing but Data Hiding
# Example : A capsule tablet contains many times of chemicals, that's it's called as Capsule.

class SampleClass(object):
    numVariable = 3691
    globalStringVariable = "Some string.."

    b = 987 # b is a global variable
    _b = 654 # can be called as protected
    __b = 321 # private

    # constrcutor.
    def __init__(self):
        self.a = 123    # OK to access directly
        self._a = 456   # should be considered protected
        self.__a = 789  # considered private, name mangled , more secure Data

    def getSecureData(self):
        print("I am a secure data",self.__a)

    def _getProtectedData(self):
        print ("inside single underscore")
        print(self.__a)

    def __getMoreSecureDataMethod(self):
        print(self.__a)

if __name__ == '__main__':
    # Lets first try to create an object of SampleClass.
    objOfSampleClass = SampleClass() # object will get created here.
    m = SampleClass() # creating another object for the same class (reason : n number of obj can be created for a class)

    # just for your reference.
    print(objOfSampleClass.b)
    print(objOfSampleClass._b)
    # If you want to bring private value/variable outside the class, normally its not possible.
    # Below is going to throw an error (uncomment and execute it)
    print(objOfSampleClass.__b)

    # But if you do still, want to bring the value outside the class. then follow the below line of code.
    # using objOfSampleClass, lets call two global variables
    print(objOfSampleClass.numVariable) # 3691
    print(objOfSampleClass.globalStringVariable) #

    # At the time of object creation, we are creating three variables Isn't it? (check __init__ method())
    # lets call those variable values one by one.
    print(objOfSampleClass.a)  # output is 123
    print(objOfSampleClass._a)  # output is 456
    #
    # print(objOfSampleClass.__a)  # uncomment and run this line, it will throw an error.
    #
    # # If you want to bring out the private attribute of a class, then please see the next time.
    print(objOfSampleClass._SampleClass__a)  # to access __a,
    # object._ClassName__privateVariable


    # below line contains getSecureData() - which is a public method, inside this method we are printing __a value,
    # it will work.
    print("calling a method: ", objOfSampleClass.getSecureData())
    print("calling a protected method: ", objOfSampleClass._getProtectedData())

    # # Below method has __ [two underscores], which is considered as private method here. So it cannot be called outside the class.
    # Uncomment the below line and test.
    # print("calling a method: ", m.__getMoreSecureData())

    # here we are tyring to get the method out, but it's not possible.
    print("calling a method: ", m._SampleClass__getMoreSecureData())
