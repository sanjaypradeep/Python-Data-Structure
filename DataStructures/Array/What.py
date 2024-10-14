# What is array?
# Array is a data structure used to store homogeneous elements at contiguous locations.
# One memory block is allocated for the entire array to hold the elements of the array. 
# The array elements can be accessed in constant time by using the index of the particular element as the subscript

# Common array operations:
# Search
# Insert
# Delete

# Time complexity:

# Search: O(n)
# Insert: O(n)
# Delete: O(n)
# Indexing: O(1)

# Disadvantage of array?
# Fixed size: The size of the array is static (specify the array size before using it, this can be overcome using Dynamic Arrays).
# One block allocation: To allocate the array itself at the beginning, sometimes it may not be possible to get the memory for the complete array (if the array size is big).
# Complex position-based insertion: To insert an element at a given position, we may need to shift the existing elements. This will create a position for us to insert the new element at the desired position. If the position at which we want to add an element is at the beginning, then the shifting operation is more expensive .

# Arrays in Python:
# Python does not have a native support for arrays, but has a more generic data structure called LIST. 
# List provides all the options as array with more functionality. But with few tweaks we can implement Array data structure in Python. 


class Array(object):
    ''' sizeOfArray: denotes the total size of the array to be initialized
       arrayType: denotes the data type of the array(as all the elements of the array have same data type)
       arrayItems: values at each position of array
    '''
    def __init__(self, sizeOfArray, arrayType = int):
        self.sizeOfArray = len(list(map(arrayType, range(sizeOfArray))))
        self.arrayItems =[arrayType(0)] * sizeOfArray    # initialize array with zeroes
        
    def __str__(self):
            return ' '.join([str(i) for i in self.arrayItems])
            
    # function for search
    def search(self, keyToSearch):
        for i in range(self.sizeOfArray):
            if (self.arrayItems[i] == keyToSearch):    # brute-forcing
                return i     # index at which element/ key was found
            
        return -1          # if key not found, return -1
    
    # function for inserting an element
    def insert(self, keyToInsert, position):
        if(self.sizeOfArray > position):
            for i in range(self.sizeOfArray - 2, position - 1, -1):
                self.arrayItems[i + 1] = self.arrayItems[i]
            self.arrayItems[position] = keyToInsert
        else:
            print('Array size is:', self.sizeOfArray)
            
    # function to delete an element
    def delete(self, keyToDelete, position):
        if(self.sizeOfArray > position):
            for i in range(position, self.sizeOfArray - 1):
                self.arrayItems[i] = self.arrayItems[i + 1]
        else:
            print('Array size is:', self.sizeOfArray)
    
a = Array(10, int)
print(a)

a.insert("Sanjay", 9)
print(a)

a.delete('Sanjay', 9)
print(a)