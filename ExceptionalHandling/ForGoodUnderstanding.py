
'''
What is Exception?

Errors detected during execution are called exceptions, if a statement or expression is syntactically correct, it may cause an error when an attempt is made to execute it. 

'''

# print(1/0) # Syntactically it's right, but do you think this will execute?

# print(name) # have we declared/defined before this line of code?

# What will be the output?

# print('2' + 5) 


# To overcome the aboev examples, I'm creating method, which handles the exeptions in it. 

# First example

def division():
    try:
        print(1/0)
    except ZeroDivisionError:
        print("why are you trying divide a natural number with 0?")
    except ValueError:
        print("Value error man..")
    except TimeoutError:
        print("time out error sir..")

division()

# Second example

def showName():
    try:
        print(name)
    except ZeroDivisionError:
        print("why are you trying divide a natural number with 0?")
    except ValueError:
        print("Value error man..")
    except TimeoutError:
        print("time out error sir..")
    except NameError:
        print("You haven't defined any such variable btw")
    # Stlyish way is..
    except (RecursionError,NameError,TypeError, ZeroDivisionError):
        print("I catched.")
        pass

showName()

# Third Example

def addValues():
    try:
        print('2' + 'Sanjay' + 1232)
    # except TypeError:
    #     print("I don't support this type.")
    except Exception:
        print("Master guy says, Something went wrong inside the code.")

addValues()

# Till now, we saw about predefined or system defined exceptions, isn't it?
# Think about writing our own exceptions?

# JFYI

'''
When we are developing a large Python program, it is a good practice to place all the user-defined 
exceptions that our program raises in a separate file. Many standard modules do this. They define their 
exceptions separately as exceptions.py or errors.py (generally but not always).


ser-defined exception class can implement everything a normal class can do, but we generally make them simple and concise. 
Most implementations declare a custom base class and derive others exception classes from this base class. 
'''

# first example of user defined exception.
class SanjayException(Exception):    
    pass


def evenOrOdd(number):
    if type(number) is not int:
        raise(SanjayException("input parameter is not in right format"))
    return True if number %2 ==0 else False

evenOrOdd('Sanjay')


# To go even deeper, here's the list of user defined exceptions.

class Error(Exception):
    """Base class for other exceptions"""
    pass


class ValueTooSmallError(Error):
    """Raised when the input value is too small"""
    pass


class ValueTooLargeError(Error):
    """Raised when the input value is too large"""
    pass


# you need to guess this number
gloal_lucky_number = 10

# user guesses a number until he/she gets it right
while True:
    try:
        userGivenInput = int(input("Enter a number: "))
        if userGivenInput < gloal_lucky_number:
            raise ValueTooSmallError
        elif userGivenInput > gloal_lucky_number:
            raise ValueTooLargeError
        break
    except ValueTooSmallError:
        print("This value is too small, try again!")
        print()
    except ValueTooLargeError:
        print("This value is too large, try again!")
        print()

print("Congratulations! You guessed it correctly.")


# Q & A ?


'''
Here's the overall predefined exception tree structure.

BaseException
 +-- SystemExit
 +-- KeyboardInterrupt
 +-- GeneratorExit
 +-- Exception
      +-- StopIteration
      +-- StandardError
      |    +-- BufferError
      |    +-- ArithmeticError
      |    |    +-- FloatingPointError
      |    |    +-- OverflowError
      |    |    +-- ZeroDivisionError
      |    +-- AssertionError
      |    +-- AttributeError
      |    +-- EnvironmentError
      |    |    +-- IOError
      |    |    +-- OSError
      |    |         +-- WindowsError (Windows)
      |    |         +-- VMSError (VMS)
      |    +-- EOFError
      |    +-- ImportError
      |    +-- LookupError
      |    |    +-- IndexError
      |    |    +-- KeyError
      |    +-- MemoryError
      |    +-- NameError
      |    |    +-- UnboundLocalError
      |    +-- ReferenceError
      |    +-- RuntimeError
      |    |    +-- NotImplementedError
      |    +-- SyntaxError
      |    |    +-- IndentationError
      |    |         +-- TabError
      |    +-- SystemError
      |    +-- TypeError
      |    +-- ValueError
      |         +-- UnicodeError
      |              +-- UnicodeDecodeError
      |              +-- UnicodeEncodeError
      |              +-- UnicodeTranslateError
      +-- Warning
           +-- DeprecationWarning
           +-- PendingDeprecationWarning
           +-- RuntimeWarning
           +-- SyntaxWarning
           +-- UserWarning
           +-- FutureWarning
	   +-- ImportWarning
	   +-- UnicodeWarning
	   +-- BytesWarning
'''