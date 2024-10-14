import operator 
import time 
  
# Defining lists 
L1 = [1, 2, 3] 
L2 = [2, 3, 4] 
  
# Starting time before map  
# function 
t1 = time.time()
  
# Calculating result 
a, b, c = map(operator.mul, L1, L2)

# Ending time after map 
# function 
t2 = time.time() 
  
# Time taken by map function 
print("Result:", a, b, c) 
print("Time taken by map function: %.6f" %(t2 - t1)) 
  
# Starting time before naive  
# method 
t1 = time.time() 
  
# Calculating result usinf for loop 
print("Result:", end = " ") 
for i in range(3): 
    print(L1[i] * L2[i], end = " ") 
      
# Ending time after naive 
# method 
t2 = time.time() 
print("\nTime taken by for loop: %.6f" %(t2 - t1)) 