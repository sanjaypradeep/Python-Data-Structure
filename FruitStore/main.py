from FStore import FStore
from FStore import Cart
import time
import getpass
import logging

import json
def getAvilableStock():
    stockInfo = open(r"FruitStore\stock.json", "r")
    return json.load(stockInfo)

openStore = FStore(getAvilableStock())
cartInstance = Cart()

def getUserInput(fromWhichMenu):

    inputMessage = ''
    if fromWhichMenu == "fromMainMenu":
        inputMessage = "Please enter your choice : "
    elif fromWhichMenu == "fruitMenu":
        inputMessage = "Please enter fruit id : "
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



def displayMainMenu():
    print("""
    1. Show available fruits        
    2. Buy Fruits                   
    3. Show Cart
    4. Checkout
    5. Exit
    6. Display available Stocks (only store admin can access)
    """)

def addMoreItems():
    if (getUserInput("addMoreItems")):
        displayFruitMenu()
        choice = getUserInput("fruitMenu")
        return choice
    else:
        print("purchase done")
        

def displayFruitMenu():
    for i in enumerate(openStore.listOfFruits(), start=1):
        print(i[0], i[1])

def billFormat(billObj):
    for fruitName, price in billObj.items():
        print(fruitName + " - " + str(price))

    print("Total Bill amount to pay " + str(sum(billObj.values())) + " Rupees \n")


def checkOutCart():
    billMap = {}
    cartItems = cartInstance.showCart()
    for fn,count in cartItems.items():
        fruitPrice = openStore.getFruitPrice(fn)
        billMap[fn] = fruitPrice * count
    billFormat(billMap)

def showAvailableFruits():
    availableFruits = openStore.listOfFruits()
    print("Here's the available fruits, happy purchasing\n")
    for id, fruit in availableFruits.items():
        print(str(id) + " - " + fruit[0] + "(each " + fruit[0] + " cost " + str(fruit[1]) + " Rupees)")   

def buyFruit(fruitId):
    if int(fruitId) in openStore.getFruitsIDs():                
        fruitCount = int(getUserInput("numbers"))
        if fruitCount  <= openStore.getAvailableCountForFruit(fruitId):
            cartInstance.addToCart(openStore.getFruitName(fruitId), fruitCount)
            openStore.updateStock(openStore.getFruitName(fruitId), fruitCount)

            print(str(fruitCount) + " " +openStore.getFruitName(fruitId) + " added to your cart \n")
        else:
            print("The count you entered is either exceeding or we nearing out of stock soon")
    else:
        print("ID which's entered isn't matching with any fruits which we have!")


if __name__ == "__main__":
    
    while True:
        displayMainMenu()
        userChoice = getUserInput("fromMainMenu")

        if userChoice == '1':
            showAvailableFruits()
        elif userChoice == '2':
            showAvailableFruits()
            choice = getUserInput("fruitMenu")
            buyFruit(choice)
            if(getUserInput("addMoreItems")):
                for i in range(len(openStore.giveAvailableFruitsInStock())):
                    showAvailableFruits()
                    choice = getUserInput("fruitMenu")
                    buyFruit(choice)
            else:
                displayFruitMenu()
        elif userChoice == '3':
            cartItems = cartInstance.showCart()
            print("Currently you have below items in your cart, ")
            for itemName, itemCount in cartItems.items():                
                print(itemName + "-" + str(itemCount))   
            time.sleep(7)     
        elif userChoice == '4':
            checkOutCart()
            print("Enjoy Shopping at Ram's Fruit Store!\n")
            break
        elif userChoice == '5':
            break 
        elif userChoice == '6':
            if(getUserInput("adminStuff")):
                openStore.displayStock()
                break
        else:
            print("Invalid input. Please enter number between 1-6 ")