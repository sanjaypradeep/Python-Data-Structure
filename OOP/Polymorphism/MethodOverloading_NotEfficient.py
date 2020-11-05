'''
1. Reason for not using class?
    Because, 
'''

# Function to take multiple arguments 
# *args is a list [1,2,3...]
def add(datatype, *args): 
  
    # if datatype is int 
    # initialize answer as 0 
    if datatype =='int': 
        answer = 0
          
    # if datatype is str 
    # initialize answer as '' 
    if datatype =='str': 
        answer ='' 
  
    # Traverse through the arguments 
    for x in args: 
  
        # This will do addition if the  
        # arguments are int. Or concatenation  
        # if the arguments are str 
        answer = answer + x 
  
    print(answer)


# Integer 
add('int', 5, 6,101,203,4354,54,65,76,4,6567,87,554,65,734,34,45,56,767,778) 
  
# String 
add('str', 'Hi ', 'Geeks', "ram", "all", 'the', 'best') 


class sampleclass():

    def __init__(self, *args):
        self.x = args
    

    def showMe(self):
        print(self.x)


ramObj = sampleclass(10,20,30,'Sanjay')
ramObj.showMe()



