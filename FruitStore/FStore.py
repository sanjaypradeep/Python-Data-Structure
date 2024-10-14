import time, sys

class Cart:
    def __init__(self):
        self.items = {}

    def addToCart(self,fruitName, quantity):
        self.items[fruitName] = quantity

    def removeFromCart(self,itemindex):
        self.items.pop(itemindex)

    def showCart(self):
        return self.items


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
        for fruits, quantity in self.stock.items():
            print("we have " + str(quantity) +  " of " + fruits)
        return '\n'
    
    def getStockFromStore(self):
        return self.stock
    
    def listOfFruits(self):
        op = {}
        for key, value in self.stock.items():
            op[value['id']] = [key, value['price']]
        return op       

    def timeDelay(self):
        self.time = time.sleep(5)
        return self.time
    
    def callExit(self):
        self.exit = sys.exit(0)
        return self.exit
    
    def getFruitsIDs(self):
        fID = []
        for key, value in self.stock.items():
            fID.append(value['id'])
        return fID

    def getAvailableCountForFruit(self, fruitID):
        for key,value in self.stock.items():
            if int(fruitID) in list(value.values()):
                # print("availab count is ", list(value.values())[0] )
                return list(value.values())[0]

    def getFruitName(self, fruitID):
        for fruitName,fruitInfo in self.stock.items():
            if int(fruitID) in list(fruitInfo.values()):
                return fruitName

    def updateStock(self, fruitName, quantity):
        fruitInfo = self.stock[fruitName]
        fruitInfo['availableCount'] = fruitInfo['availableCount'] - quantity
        # print(self.stock)

    def getFruitPrice(self, fruitName):
        for fn, value in self.stock.items():
            if fruitName == fn:
                return value['price']

    def giveAvailableFruitsInStock(self):
        op = []
        for fn, fInfo in self.stock.items():
            if fInfo['availableCount'] > 0:
                op.append(fn)
        return op
    
    def showAvailableFruits(self):
        availableFruits = self.listOfFruits()
        print("Here's the available fruits, happy purchasing\n")
        for id, fruit in availableFruits.items():
            print(str(id) + " - " + fruit[0] + "(each " + fruit[0] + " cost " + str(fruit[1]) + " Rupees)")