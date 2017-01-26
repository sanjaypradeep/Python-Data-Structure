__author__ = 'Sanjay'

# Here is the real time scenario for Dynamic Programming.
# A classic example of an optimization problem involves making change using the fewest coins.
# Suppose you are a programmer for a vending machine manufacturer. Your company wants to streamline effort
# by giving out the fewest possible coins in change for each transaction. Suppose a customer puts in a
#  dollar bill and purchases an item for 37 cents. What is the smallest number of coins you can use to
# make change? The answer is six coins: two quarters, one dime, and three pennies. How did we arrive at
# the answer of six coins? We start with the largest coin in our arsenal (a quarter) and use as many of
#  those as possible, then we go to the next lowest coin value and use as many of those as possible.

def dpMakeChange(coinValueList,change,minCoins,coinsUsed):
   for cents in range(change+1):
      coinCount = cents
      newCoin = 1
      for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents-j] + 1 < coinCount:
               coinCount = minCoins[cents-j]+1
               newCoin = j
      minCoins[cents] = coinCount
      coinsUsed[cents] = newCoin
   return minCoins[change]

def printCoins(coinsUsed,change):
   coin = change
   while coin > 0:
      thisCoin = coinsUsed[coin]
      print(thisCoin)
      coin = coin - thisCoin

def main():
    amnt = 63
    clist = [1,5,10,21,25]
    coinsUsed = [0]*(amnt+1)
    coinCount = [0]*(amnt+1)

    print("Making change for",amnt,"requires")
    print(dpMakeChange(clist,amnt,coinCount,coinsUsed),"coins")
    print("They are:")
    printCoins(coinsUsed,amnt)
    print("The used list is as follows:")
    print(coinsUsed)

if __name__ == '__main__':
    main()

