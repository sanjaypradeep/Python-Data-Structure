__author__ = 'Sanjay'


#Testing for 25 with octal (8)

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
        print (self.items)
        return self.items

    def peek(self):
         return self.items[0]

    def size(self):
        return len(self.items)


def baseConverter(decNumber,base): #(25,8)
    digits = "0123456789ABCDEF"

    remstack = Stack()

    while decNumber > 0: #True, 3
        rem = decNumber % base # 25%8 = 1, 3 %8 = 3
        remstack.push(rem) # pushing inside the empty stack, [1,3]
        decNumber = decNumber # 25//8 = 3 ,3//8 = 0

    newString = ""
    while not remstack.isEmpty():
        newString = newString + digits[remstack.pop()]

    return newString

print(baseConverter(25,2))
print(baseConverter(25,16))