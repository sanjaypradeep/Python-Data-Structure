# If you want to run the below code, you need a python library
# pip3 install multipledispatch



from multipledispatch import dispatch 
  
#passing one parameter 
@dispatch(int,int) # this is called as `property`
def product(first,second): 
    result = first*second 
    print(result); 
  
#passing two parameters 
@dispatch(int,int,int) 
def product(first,second,third): 
    result  = first * second * third 
    print(result); 
  
#you can also pass data type of any value as per requirement 
@dispatch(float,float,float) 
def product(first,second,third): 
    result  = first * second * third 
    print(result); 
  
  
#calling product method with 2 arguments 
product(2,3,2) #this will give output of 12 
product(2.2,3.4,2.3) # this will give output of 17.985999999999997 
