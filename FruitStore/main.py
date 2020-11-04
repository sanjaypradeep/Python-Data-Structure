from FStore import FStore

# TODO 1 - get stock from reading a json file. 
dict = {'Apple':100, 'Banana': 100, 'Cherry': 100}
# Write a function to read stock json file
# function should return json info which is there in the file.


# TODO 2 - pass the return of above function, to open your store
openStore = FStore(dict) # you cannot open a store without stock.

def getUserInput(fromWhichMenu):

    if fromWhichMenu == "fromMainMenu":
        try:
            choice = input("Please enter your choice : ").strip()
        except ValueError:
            print("That's not an int!")
        return choice
    elif fromWhichMenu == "fruitMenu":
        try:
            choice = input("Please enter your choice : ").strip()
        except ValueError:
            print("That's not an int!")
        return choice
    elif fromWhichMenu == "numbers":
        try:
            choice = input("how many you need? ").strip()
        except ValueError:
            print("That's not an int!")
    
        return choice
    elif fromWhichMenu == "addOrRemove" :
        try:
            choice = input("Is there anything you want to add or remove? Y or N ").strip()
            if choice == "Y":
                return True
            else:
                return False
        except ValueError:
            print("That's not an int!")



def displayMainMenu():
    print("""
    ====== Fruit Shop =======
    1. Display available Stocks
    2. Buy Fruits
    3. Get Total
    4. Checkout
    5. Exit
    """)

def displayFruitMenu():
    for i in enumerate(openStore.listOfFruits(), start=1):
        print(i[0], i[1])

def shoppingCart():
    pass

def storeOpens():
    # while True:
    cart = {}      
    displayMainMenu()
    choice = getUserInput("fromMainMenu")

    if choice == '1':
        openStore.displayStock()
        print("\n please select from above available stock", end="\n")
    elif choice == '2':
        print("\n What do you want to buy?\n")
        displayFruitMenu()
        choice = getUserInput("fruitMenu")

        if choice == '1': 
            availableStock = openStore.getStockFromStore()
            count = int(getUserInput("numbers"))

            if count  <= availableStock['Apple']:
                cart['Apple'] = count
                availableStock['Apple'] = availableStock['Apple'] - count
                print(availableStock)

            print("Here's your items in cart  , ", cart)
            # wannaBuyMore = getUserInput("addOrRemove")
            # if (wannaBuyMore):
            #     fruitChoice = getUserInput("fruitMenu")

            # else:
            #     print("Done")

            
        elif choice == '2':
            pass
        elif choice == '3':
            pass            

    elif choice == 5:
        pass          
    else:
        print("Invalid input. Please enter number between 1-5 ")


if __name__ == "__main__":
    storeOpens()