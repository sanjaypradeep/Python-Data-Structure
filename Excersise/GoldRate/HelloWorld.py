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

def setTwoFour1G(priceToSet):
    gold_rate['24K']['1g'] = priceToSet

def setGoldPrice(K, g, price):
    # if(K != '24K' or K != '22K'):
    #     return "Values given for K, isn't accepted."
    # if(g != '1g' or g != '8g'):
    #     return "Values give for g, isn't accepted."
    gold_rate[K][g] = price 

def getDateFormat():
    import datetime
    todayDateInfo = datetime.datetime.now()   
    output= str(todayDateInfo.day) +'/' + str(todayDateInfo.strftime("%B")) + "/" + str(todayDateInfo.year) 
    print(output)
    return output

import requests 
from bs4 import BeautifulSoup 
  
URL = "https://www.livechennai.com/gold_silverrate.asp"
r = requests.get(URL) 
  
soup = BeautifulSoup(r.content, 'html5lib') 

table = soup.find('table', attrs = {'class':'table-price'}) 

tempData = table.get_text()


allData = list(tempData.split(" "))

listOfText = [i for i in allData if i]

finalList = [i for i in listOfText if i != '\n']
#print(test_list)

indexValue = finalList.index(getDateFormat()+'\n')
# print(indexValue)

setGoldPrice('22K', '1g', finalList[indexValue+3])
setGoldPrice('22K' , '8g', finalList[indexValue+4])

setGoldPrice('24K', '1g', finalList[indexValue+1])
setGoldPrice('24K', '8g', finalList[indexValue+2])

# gold_rate['24K']['1g'] =  finalList[indexValue+1]
# gold_rate['24K']['8g'] =  finalList[indexValue+2]
# gold_rate['22K']['1g'] =  finalList[indexValue+3]
# gold_rate['22K']['8g'] =  finalList[indexValue+4]

print("24K Gold - 1 Gram price is " + gold_rate['24K']['1g'])

print("24K Gold - 8 Gram price is " + gold_rate['24K']['8g'])

print("22K Gold - 1 Gram price is " + gold_rate['22K']['1g'])

print("22K Gold - 8 Gram price is " + gold_rate['22K']['8g'])

import time
time.sleep(15)