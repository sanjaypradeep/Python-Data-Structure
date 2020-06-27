

# Have you heard about State in Programming Language?

# Very frequentlt this terminology is been used in Entity or Object Communication. 


# Let's say we have to model a bank account with support for deposit and withdraw operations. 
# One way to do that is by using global state

balance = 0 #balance variable is global of the program, if this below snippet is inside the class, we can call as class attribute.

def deposit(amount):
    global balance
    balance += amount
    return balance

def withdraw(amount):
    global balance
    balance -= amount
    return balance

sanjay = deposit(100)
print(sanjay)

# The above example is good enough only if we want to have just a single account. 

# ******Things start getting complicated if want to model multiple accounts.******

