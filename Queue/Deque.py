__author__ = 'Sanjay'

# A deque, also known as a double-ended queue, is an ordered collection of items similar to the queue.
# It has two ends, a front and a rear, and the items remain positioned in the collection.
# What makes a deque different is the unrestrictive nature of adding and removing items.
# New items can be added at either the front or the rear.
# Likewise, existing items can be removed from either end.
# it does not require the LIFO and FIFO orderings that are enforced by those data structures.
# It is up to you to make consistent use of the addition and removal operations.

# Deque() creates a new deque that is empty. It needs no parameters and returns an empty deque.

# addFront(item) adds a new item to the front of the deque. It needs the item and returns nothing.

# addRear(item) adds a new item to the rear of the deque. It needs the item and returns nothing.

# removeFront() removes the front item from the deque. It needs no parameters and returns the item. The deque is modified.

# removeRear() removes the rear item from the deque. It needs no parameters and returns the item. The deque is modified.

# isEmpty() tests to see whether the deque is empty. It needs no parameters and returns a boolean value.

# size() returns the number of items in the deque. It needs no parameters and returns an integer.

class Deque:
    def __init__(self):
        self.items = []

    def addFront(self,item):
        self.items.append(item)

    def addRear(self,item):
        self.items.insert(0,item)

    def removeFront(self):
        self.items.pop()

    def removeRear(self):
        self.items.pop(0)

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

if __name__ == '__main__':
    d=Deque()
    print(d.isEmpty())
    d.addRear(4)
    d.addRear('dog')
    d.addFront('cat')
    d.addFront(True)
    print(d.size())
    print(d.isEmpty())
    d.addRear(8.4)
    print(d.removeRear())
    print(d.removeFront())