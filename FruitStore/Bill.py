

class BillFormatter:

    def __init__(self, billMap):
        self.billObj = billMap

    def generateBill(self):
        for fruitName, price in self.billObj.items():
            print(fruitName + " - " + str(price))

        print("Total Bill amount to pay " + str(sum(self.billObj.values())) + " Rupees \n")