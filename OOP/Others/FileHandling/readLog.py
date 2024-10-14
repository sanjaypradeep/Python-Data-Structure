from collections import Counter


with open('C:\\Users\\sanja\\Documents\\GitHub\\Python-Data-Structure\\OOP\\Others\\FileHandling\\ram.txt', 'r+') as info:    
    info = info.readlines()

# print(info)

commandList = ['connected', 'disconnected']
exchangeList= ['exchange_sanjay_x', 'exchange_sanjay_y']

count = 0

sampleList= []

connectedList = []
disconnectedList = []

output = {}

for lines in info:
    splittedInfo = lines.split(" ")
    for exchangeName in exchangeList:
        if exchangeName in splittedInfo and 'connected' in splittedInfo:
            connectedList.append(exchangeName)
        if exchangeName in splittedInfo and 'disconnected' in splittedInfo:
            disconnectedList.append(exchangeName)
        

print(dict(Counter(connectedList)))
print(dict(Counter(disconnectedList)))


{
    'exchange_sanjay_x': {
        'timeStamp': '12:00:57',
        'connectedCount': 4
        'disconnectedCount': 2
    }

}