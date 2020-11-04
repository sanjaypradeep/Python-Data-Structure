import time, sys

class FStore:


    def __init__(self, stock={}):
        """
        Our constructor class that instantiates fruit store.
        """
        self.stock =  stock
    
    def displayStock(self):
        """
        Displays the fruits currently available for purchase in the store.
        """

        # for fruits, quantity in self.stock.items():
        #     print(" We currently have {} {} in store".format(quantity, fruits), end="\n")
        
        # return None

        # Sanjay's code
        for fruits, quantity in self.stock.items():
            print("we have " + str(quantity) +  " of " + fruits)

        return '\n'
    
    def getStockFromStore(self):
        return self.stock
    
    def listOfFruits(self):
        # self.Fruits = [fruits for fruits in self.stock.keys()]
        # return self.Fruits

        # Sanjay's code
        return list(self.stock.keys())
            

    def timeDelay(self):
        self.time = time.sleep(5)
        return self.time
    
    def callExit(self):
        self.exit = sys.exit(0)
        return self.exit

    def numberOfFruits(self, number):

        # if number <= 0:
        #     print("Number of fruits should be positive!")
        #     return None 
        # elif n > self.stock.values()[0]
        pass

    def cart(self):
        # cart logic
        pass



# TODO: 3 - crate a class called ShoppingCart
# addToCart
# ṛemoveFromCart
# getListOfItemsFromCart

