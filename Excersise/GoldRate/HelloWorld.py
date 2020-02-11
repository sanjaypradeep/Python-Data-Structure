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
# print(len(allData))
# print(allData.count(''))
# print(allData.count("\n"))

test_list1 = [i for i in allData if i]

test_list = [i for i in test_list1 if i != '\n']
#print(test_list)

indexValue = test_list.index(getDateFormat()+'\n')
# print(indexValue)

# goldRate24_1gram = test_list[indexValue+1]

gold_rate['24K']['1g'] =  test_list[indexValue+1]
gold_rate['24K']['8g'] =  test_list[indexValue+2]
gold_rate['22K']['1g'] =  test_list[indexValue+3]
gold_rate['22K']['8g'] =  test_list[indexValue+4]

print("24K Gold - 1 Gram price is " + gold_rate['24K']['1g'])

print("24K Gold - 8 Gram price is " + gold_rate['24K']['8g'])

print("22K Gold - 1 Gram price is " + gold_rate['22K']['1g'])

print("22K Gold - 8 Gram price is " + gold_rate['22K']['8g'])

import time
# time.sleep(15)

import datetime
