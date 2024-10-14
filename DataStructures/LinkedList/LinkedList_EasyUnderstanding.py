# Like arrays, Linked List is a linear data structure.
# Unlike arrays, linked list elements are not stored at a contiguous location; the elements are linked using pointers.

# Why Linked List?
# Arrays can be used to store linear data of similar types, but arrays have the following limitations.
# 1) The size of the arrays is fixed: So we must know the upper limit on the number of elements in advance. Also, generally, the allocated memory is equal to the upper limit irrespective of the usage.
# 2) Inserting a new element in an array of elements is expensive because the room has to be created for the new elements and to create room existing elements have to be shifted.

# A simple Python program to introduce a linked list

# Node class
class Node:

    # Function to initialise the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null


# Linked List class contains a Node object
class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    # This function prints contents of linked list
    # starting from head
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end=",")
            temp = temp.next


# Code execution starts here
if __name__ == '__main__':
    # Start with the empty list
    llist = LinkedList()
    print(llist) #instance of LinkedList Class.
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)

    ''' 
    Three nodes have been created. 
    We have references to these three blocks as head, 
    second and third 

    llist.head        second              third 
         |                |                  | 
         |                |                  | 
    +----+------+     +----+------+     +----+------+ 
    | 1  | None |     | 2  | None |     |  3 | None | 
    +----+------+     +----+------+     +----+------+ 
    '''

    llist.head.next = second  # Link first node with second

    ''' 
    Now next of first Node refers to second.  So they 
    both are linked. 

    llist.head        second              third 
         |                |                  | 
         |                |                  | 
    +----+------+     +----+------+     +----+------+ 
    | 1  |  o-------->| 2  | null |     |  3 | null | 
    +----+------+     +----+------+     +----+------+  
    '''

    second.next = third # Link second node with the third node

    ''' 
    Now next of second Node refers to third.  So all three 
    nodes are linked. 

    llist.head        second              third 
         |                |                  | 
         |                |                  | 
    +----+------+     +----+------+     +----+------+ 
    | 1  |  o-------->| 2  |  o-------->|  3 | null | 
    +----+------+     +----+------+     +----+------+  
    '''
    llist.printList()