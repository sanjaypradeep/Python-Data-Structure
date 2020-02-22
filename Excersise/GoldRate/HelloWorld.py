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


import requests 
from datetime import date
from bs4 import BeautifulSoup 

  
URL = "https://www.livechennai.com/gold_silverrate.asp"
r = requests.get(URL) 
  
soup = BeautifulSoup(r.content, 'html5lib') 

table = soup.find('table', attrs = {'class':'table-price'}) 

tempData = table.get_text()


allData = list(tempData.split(" "))


test_list1 = [i for i in allData if i]

test_list = [i for i in test_list1 if i != '\n']

todayDate = "11/February/2020\n"

dateObj = date.today()

todayDate = dateObj.strftime("%d") + "/" + dateObj.strftime("%B") + "/" + dateObj.strftime("%Y") + "\n" 
todaysDateFormatToDB = dateObj.strftime("%Y")+'-'+dateObj.strftime("%m")+'-'+dateObj.strftime("%d")

try:
    indexValue = test_list.index(todayDate)
except Exception as ex:
    print("Error Info: " + ex)

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
#time.sleep(25)

import mysql.connector
from mysql.connector import Error

def connectToDB():
    try:

        connection = mysql.connector.connect(host='localhost',
                                            database='world',
                                            user='root',
                                            password='root')
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)
            return connection
    except Error as e:
        print("Error while connecting to MySQL", e)


def insertRecord(con):
    if con.is_connected():
        # print("=======================================")
        # print(todaysDateFormatToDB)
        # print(gold_rate['24K']['8g'])
        # print(gold_rate['24K']['1g'])
        # print(gold_rate['22K']['8g'])
        # print(gold_rate['22K']['1g'])

        # sample = []
        # sample.insert(0, todaysDateFormatToDB)
        # sample.insert(1, gold_rate['24K']['8g'])
        # sample.insert(2, gold_rate['24K']['1g'])
        # sample.insert(3, gold_rate['22K']['8g'])
        # sample.insert(4, gold_rate['22K']['1g'])

        # print("finally...." , sample)
        # print("=======================================")

        mySql_insert_query = """INSERT INTO `world`.`daily_gold_rates` (`todays_date`, 
													`twentyFour_carot_eight_grams`, 
													`twentyFour_carot_one_gram`, 
													`twentyTwo_carot_eight_grams`, 
													`twentyTwo_carot_one_gram` ) 
                                VALUES ('2019-08-14', '33455', '4252', '31253', '4072');"""

        something = "INSERT INTO `world`.`daily_gold_rates` (`todays_date`, `twentyFour_carot_eight_grams`,`twentyFour_carot_one_gram`, `twentyTwo_carot_eight_grams`, `twentyTwo_carot_one_gram` ) VALUES ('" + str(todaysDateFormatToDB) +"','"+ gold_rate['24K']['8g'] +"'," + "'"+gold_rate['24K']['1g']+ "'," + "'"+ gold_rate['22K']['8g'] +"',"+ "'" + gold_rate['22K']['1g'] +"'" +");" 

        # print(something)
        # time.sleep(10)

        # something2 = "INSERT INTO `world`.`daily_gold_rates` (`todays_date`, `twentyFour_carot_eight_grams`,`twentyFour_carot_one_gram`,`twentyTwo_carot_eight_grams`,`twentyTwo_carot_one_gram`  ) VALUES (" +str(sample[0]) +',' + sample[1] +',' + sample[2]+','+ sample[3]+','+sample[4]+');'

        # print("something2.. ", something2)
        # time.sleep(10)

        # something = "INSERT INTO `world`.`daily_gold_rates` (`todays_date`, `twentyFour_carot_eight_grams`, `twentyFour_carot_one_gram`, `twentyTwo_carot_eight_grams`, `twentyTwo_carot_one_gram` ) VALUES (" + todaysDateFormatToDB +");" 

        cursor = con.cursor()
        cursor.execute(something)
        con.commit()
        print(cursor.rowcount, "Record inserted successfully into Laptop table")
        # con.close()

def disconnectDB(con):
        if (con.is_connected()):
            con.close()
            print("MySQL connection is closed")

connectionHook = connectToDB()
insertData = insertRecord(connectionHook)
diconnect = disconnectDB(connectionHook)
