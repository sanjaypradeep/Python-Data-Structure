from FStore import FStore, Cart
from Bill import BillFormatter


import json
def getAvilableStock():
    stockInfo = open(r"FruitStore\stock.json", "r")
    return json.load(stockInfo)

openStore = FStore(getAvilableStock())
cartInstance = Cart()

class StoreHandler:
    def __init__(self):
        openStore = FStore(getAvilableStock())
        userInstance = UserHandler()
    
    def showAvailableFruitsFromStore(self):
        self.openStore.showAvailableFruits()

    def buyFruit(self, fruitId):
        if int(fruitId) in self.openStore.getFruitsIDs():                
            fruitCount = int(self.userInstance.getUserInput("numbers"))
            if fruitCount  <= self.openStore.getAvailableCountForFruit(fruitId):
                cartInstance.addToCart(self.openStore.getFruitName(fruitId), fruitCount)
                self.openStore.updateStock(openStore.getFruitName(fruitId), fruitCount)

                print(str(fruitCount) + " " +self.openStore.getFruitName(fruitId) + " added to your cart \n")
            else:
                print("The count you entered is either exceeding or we nearing out of stock soon")
        else:
            print("ID which's entered isn't matching with any fruits which we have!")



class CartHandler:
    def __init__(self):
        cartHandlerInstance = Cart()
    
    def showCart(self):
        return self.cartHandlerInstance.showCart()

    def checkOutCart(self):
        billMap = {}
        cartItems = self.cartHandlerInstance.showCart()
        for fn,count in cartItems.items():
            fruitPrice = openStore.getFruitPrice(fn)
            billMap[fn] = fruitPrice * count
        
        billInstance = BillFormatter(billMap)
        billInstance.generateBill()

    

class UserHandler:
    def __init__(self):
        pass

    def showMainMenu(self):
        print("""
            1. Show available fruits        
            2. Buy Fruits                   
            3. Show Cart
            4. Checkout
            5. Exit
            6. Display available Stocks (only store admin can access)
        """)

    def getUserInput(self, fromWhichMenu):
        inputMessage = ''
        if fromWhichMenu == "fromMainMenu":
            inputMessage = "Please enter your choice : "
        elif fromWhichMenu == "fruitMenu":
            inputMessage = "Please enter your choice : "
        elif fromWhichMenu == "numbers":
            inputMessage = "how many you need? "
        elif fromWhichMenu == "addMoreItems":
            try:
                choice = input("Do you want to add more items to your cart? Y or N ").strip()
                if choice == "Y" or choice == "y" or choice == "yes" or choice == "YES":
                    return True
                else:
                    return False
            except ValueError:
                print("That's not an int!")
        elif fromWhichMenu == "adminStuff":
            try:
                choice = getpass.getpass("Enter admin password")
                if choice == "admin123":
                    return True
                else:
                    return False
            except ValueError:
                print("That's not a valid password!")
        
        try:
            choice = input(inputMessage).strip()
        except ValueError:
            print("That's not an int!")

        return choice 

    def mainMenuHandler(self, menuId):
        if menuId == '1' or menuId == 1:
            openStore.showAvailableFruits()
        elif menuId == '2' or menuId == 2:
            openStore.showAvailableFruits()
            choice = self.getUserInput("fruitMenu")
            storeHandlerInstance = StoreHandler().buyFruit(choice)
            # buyFruit(choice)
        elif menuId == '4' or menuId == 4:
            CartHandler.checkOutCart()
