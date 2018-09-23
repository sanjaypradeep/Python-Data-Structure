# One line defition -  A decorator takes in a function, adds some functionality and returns it.

# Description: This is also called metaprogramming as a part of the program tries to modify another part of the program at compile time.

# Prerequisites

# We must be comfortable with the fact that, everything in Python (Yes! Even classes), are objects.
# Names that we define are simply identifiers bound to these objects. Functions are no exceptions,
# they are objects too (with attributes). Various different names can be bound to the same function object.

# Lets take the below example

def first(msg):
    print (msg)


first("Hey") #output : Hey

secondVariable = first # assinging first method to secondVariable.

secondVariable("Hello..") #output : Hello

# When you run the code, both functions first and secondVariable gives same output. Here, the names first and secondVariable refer to the same function object.
#
# Now things start getting weirder.
#
# Functions can be passed as arguments to another function.
#
# If you have used functions like map, filter and reduce in Python, then you already know about this.

# Here's the example.

def add(firstInput, secondInput):
    return firstInput + secondInput

def sub(firstInput, secondInput):
    return firstInput - secondInput

def operation(func, firstInput, secondInput):
    result = func(firstInput, secondInput)
    return result

# Here you go ..

output = operation(add, 10, 10) # assinging the result to a variable, because operation method is going to return a value

print (output) #output : 20

# Further more, a sample example..

def is_called():
    def is_returned():
        print("Hello")
    return is_returned

new = is_called()
print (new())

#Here's the Output below ..
# "Hello"
# None - basically is_called function returns is_returned method (which in turn prints "hello") so this throws None.





