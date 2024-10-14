from collections import Counter

def moveZerosToEnd(inputList):
    if type(inputList) is not list:
        return
    
    if 0 in inputList :
        ex = dict(Counter(inputList))   
        if (0 in ex.keys()):
            op = [i for i in inputList if i != 0]    
            for i in range(ex[0]):
                op.append(0) 
    else:
         return "No Zeros exist"
    

    print(op)


# OMKAR solution - isn't working.
# def move(arr):
#     count = 0
#     for a in arr:
#         if not a == 0:
#             arr[count] = a
#             count += 1
#     while count < len(nums):
#         arr[count] = 0
#         count += 1
    


moveZerosToEnd([1,2,3,4,0,0,0,0,3,4,43,43,435453,545455,7676])
print(moveZerosToEnd([1,2,3,4,4]))

