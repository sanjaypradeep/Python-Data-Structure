__author__ = 'Sanjay'

#
# Stack() creates a new stack that is empty. It needs no parameters and returns an empty stack.

# push(item) adds a new item to the top of the stack. It needs the item and returns nothing.

# pop() removes the top item from the stack. It needs no parameters and returns the item. The stack is modified.

# peek() returns the top item from the stack but does not remove it. It needs no parameters. The stack is not modified.

# isEmpty() tests to see whether the stack is empty. It needs no parameters and returns a boolean value.

# size() returns the number of items on the stack. It needs no parameters and returns an integer.


#The above information gives you clear understanding on Stacks Predefined functions.
class Stack:
    def __init__(self):
        self.items = []

    def push(self, newItem):
        self.items.append(newItem)

    def pop(self):
        self.items.pop()

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def show(self):
        print self.items
        return self.items

    def peek(self):
         return self.items[0]

    def size(self):
        return len(self.items)


if __name__ ==  '__main__':
    obj = Stack()
    obj.push(13)
    obj.show()
    obj.push('sanjay')
    obj.push('surya')
    obj.push(45)
    obj.show()
    obj.pop()
    obj.show()
    obj.size()
    obj.isEmpty()
    obj.show()
