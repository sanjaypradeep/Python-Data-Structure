

# Important point to be noted.

# finally block is always executed after leaving the try statement. 
# In case if some exception was not handled by except block, it is re-raised after execution of finally block.
# finally block is used to deallocate the system resources.
# One can use finally just after try without using except block, but no exception is handled in that case.

# here's the sample exercise for understanding `finally` keyword in python
 
try: 
    inFromUser = int(input("Hello user, give me a integer input: "))
    k = 5//inFromUser # raises divide by zero exception. 
    print(k) 
  
# handles zerodivision exception     
except ZeroDivisionError:    
    print("Can't divide by zero") 
except TypeError:
    print("Given in put is not in a right datatype")
      
finally: 
    # this block is always executed  
    # regardless of exception generation. 
    print('This is always executed') 



