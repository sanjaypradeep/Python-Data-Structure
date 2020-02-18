print("Hello world")

gold_rate = {
    "24K" : {
        "1g": "",
        "8g": ""
    },
    "22K": {
        "1g": "",
        "8g": ""
    }
}

def setGoldPrice(K, g, price):
    gold_rate[K][g] = price 

def getDateFormat():
    import datetime
    todayDateInfo = datetime.datetime.now()   
    return str(todayDateInfo.day) +'/' + str(todayDateInfo.strftime("%B")) + "/" + str(todayDateInfo.year)         

def getIndexValueOfTodaysDate():
    return finalList.index(getDateFormat()+'\n')

import requests 
from bs4 import BeautifulSoup 
  
URL = "https://www.livechennai.com/gold_silverrate.asp"
r = requests.get(URL) 
  
soup = BeautifulSoup(r.content, 'html5lib') 

table = soup.find('table', attrs = {'class':'table-price'}) 

#OverAll table date is assinged to the below variable. 
overAllTableData = table.get_text()

#Separating each table text and assigning into list.
allData = list(overAllTableData.split(" "))

# remove all empty string elements inside the list.
listOfText = [i for i in allData if i]

# removes all independent \n elements inside the list.
finalList = [i for i in listOfText if i != '\n']

indexValue = getIndexValueOfTodaysDate()

setGoldPrice('22K', '1g', finalList[indexValue+3])
setGoldPrice('22K' , '8g', finalList[indexValue+4])

setGoldPrice('24K', '1g', finalList[indexValue+1])
setGoldPrice('24K', '8g', finalList[indexValue+2])

print("24K Gold - 1 Gram price is " + gold_rate['24K']['1g'])
print("24K Gold - 8 Gram price is " + gold_rate['24K']['8g'])

print("22K Gold - 1 Gram price is " + gold_rate['22K']['1g'])
print("22K Gold - 8 Gram price is " + gold_rate['22K']['8g'])

import time
time.sleep(15)