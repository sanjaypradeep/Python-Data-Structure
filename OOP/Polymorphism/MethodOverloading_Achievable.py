# If you want to run the below code, you need a python library
# pip3 install multipledispatch



# from multipledispatch import dispatch 
  

# @dispatch(int,int) # this is called as `Decorator`
# def product(first,second): 
#     result = first*second 
#     print(result); 
  

# @dispatch(int,int,int) 
# def product(first,second,third): 
#     result  = first * second * third 
#     print(result); 
  

# @dispatch(float,float,float) 
# def product(first,second,third): 
#     result  = first * second * third 
#     print(result); 


# @dispatch(float,int,int) 
# def product(first,second,third): 
#     result  = first * second * third 
#     print(result); 

# @dispatch(int,int,float) 
# def product(first,second,third): 
#     result  = first * second * third 
#     print(result); 
  
  
#calling product method with 3 arguments 
# product(2,3,2) #this will give output of 12 
# product(2.2,3.4,2.3) # this will give output of 17.985999999999997 


# def add(a,b):
#     return a+b

# def add(a,b,c):
#     return a+b+c


# add(10,20)

def productAdd(*args):
    sampleList = list(args)    
    print(sampleList)

    # check = all(isinstance(x, str) for x in sampleList)
    # if(check):
    #     op = ''
    #     for ele in sampleList:
    #         op += ele + ' '
    #     return op
    # else:
    #     if len(sampleList) > 0:
    #         for num in sampleList:
    #             counter += num # is same as to counter = counter + num
    #     return counter

    strList = []
    intList = []
    floatList = []
    for i in sampleList:
        if type(i) is int:
            intList.append(i)
        elif type(i) is float:
            floatList.append(i)
        elif  type(i) is str:
            strList.append(i)
    
    if len(strList) > 0:
        op = ''
        for ele in strList:
            op += ele + ' '
        print(op)
    if (len(intList) > 0):
        print(sum(intList))
    # same for float as well.
        
test = productAdd(1,2,3,4,5,5,5454)
print(test)

test2 = productAdd("sanjay", "kid1", "kid2") #sanjay kid1 kid2
print(test2)

test4 = productAdd("sanjay", 1, 3, 4, 45, "tets")
print(test4)

# @dispatch(str, str, str)
# def addProduct(firstStr, secondStr, thirdStr):
#     op = ''
#     op += firstStr + secondStr + thirdStr
#     return op


# test3 = addProduct("sanjay", "kid1", "kid2")
