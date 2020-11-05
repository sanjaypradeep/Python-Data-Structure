
class Father():

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def role(self):
        print("Father of two childres")

    def occupation(self):
        print("Father is working in Bank")

    def travellingIn(self):
        print("As a father, I use Audi Car to go office")

class Mother(Father):

    def __init__(self,):
        print ("b constructor")
    
    def role(self):
        print("Mother of Two childrens")
    
    def occupation(self):
        print("Home maker")

    def whatCooking(self):
        print("Mother is preparing Pasta!")


class Son(Father, Mother):
    pass

class Son(Mother):
    pass

# creating an object of mother.
instanceOfMother = Mother()

instanceOfMother.role()

instanceOfMother.occupation()

instanceOfMother.whatCooking()

instanceOfMother.travellingIn()


# creating an object of Father

fatherInstance = Father(10,20)

fatherInstance.role()

fatherInstance.travellingIn()

fatherInstance.occupation()

fatherInstance.whatCooking() ## this will throw error