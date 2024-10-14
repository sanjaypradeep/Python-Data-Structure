

def squareNumber(n):
    if type(n) == int:        
        return n*n
    else:
        return 0

def checkForEven(n):
    if type(n) is not int:
        return
    return n%2 ==0 

def add(x, y):
    return x+y
print(squareNumber(10))

# if you want to pass a list as a  parameter, then will the above function (add()) block will support?

# NO

sampleList =[1,2,3,4,5]
outputList = []
for i in sampleList:
    outputList.append(squareNumber(i))

print(outputList)


outputList2 = []
for i in sampleList:
    if checkForEven(i):
        outputList2.append(i)    
print("output list 2 is ", outputList2)
# ===================================================

evenNum = list(filter(lambda  x: x%2 ==0, sampleList))
print(evenNum)


sqNum = list(map(squareNumber, sampleList))
print("sqNum is .. ", sqNum)

globalExample = map(lambda x, y: (x+y, x-y, x*y), [10, 20, 30, 40],[5,10,15,20])
globalExample = map(lambda x, y: (x+y, x-y, x*y), [10, 20, 30, 40],[5,10,15,20])
print(list(globalExample))





# List of strings 
l = ['sat', 'bat', 'cat', 'mat'] 

opList = []
for i in l:
    opList.append(list(i))
print(opList)

map(list, l)



# class calculator:    
#     add = lambda x,y: x+y
#     sub = lambda x,y: x-y
#     mul = lambda x,y: x*y

#     def add(a,b):
#         return a+b

# print("here you go ...")

# cal = calculator()

# print(calculator.add(10,5))

