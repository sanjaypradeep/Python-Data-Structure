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


# HERE'S SOMETHING IMPORTANT ..

# Functions and methods are called callable as they can be called.
#
# In fact, any object which implements the special method __call__() is termed callable. So, in the most basic sense, a decorator is a callable that returns a callable.
#
# Basically, a decorator takes in a function, adds some functionality and returns it.


def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner

def ordinary():
    print("I am ordinary")


# Above we have two functions.. ordinary and make_pretty()

ordinary() #output : "I am ordinary"

# Now passing ordinary() as a parameter to make_pretty

sample = make_pretty(ordinary)
sample()

# Here's the output..

# I got decorated
# I am ordinary

# Generally, we decorate a function and reassign it as,
#
# ordinary = make_pretty(ordinary).
# This is a common construct and for this reason, Python has a syntax to simplify this.
#
# We can use the @ symbol along with the name of the decorator function and place it above the definition of the function to be decorated. For example,
#
@make_pretty
def ordinary():
    print("I am ordinary")

# is equivalent to

def ordinary():
    print("I am ordinary")
ordinary = make_pretty(ordinary)

# Decorating Functions with Parameters
# The above decorator was simple and it only worked with functions that did not have any parameters. What if we had functions that took in parameters like below?

def smart_divide(func):
   def inner(a,b):
      print("I am going to divide",a,"and",b)
      if b == 0:
         print("Whoops! cannot divide")
         return

      return func(a,b)
   return inner

@smart_divide
def divide(a,b):
    return a/b

divide(5,2) # Output: I am going to divide 5 and 2

print (divide(5,2))

# Here's the Output of above statement ..

# I am going to divide 5 and 2
# 2.5


def parentFun(func):
    def internalFun():
        print("inside internal")
        func()
    return internalFun


parentFun(ordinary())
