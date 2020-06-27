

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

# The above example is good enough only if we want to have just a single account. Did you understand what I said?


# ******Things start getting complicated if want to model multiple accounts.******

# We can solve the problem by making the state local, probably by using a dictionary to store the state.

def make_account():
    return {'balance': 0}

def putDeposit(account, amount):
    account['balance'] += amount
    return account['balance']

def withdrawMoney(account, amount):
    account['balance'] -= amount
    return account['balance']

def checkBalance(account):
    return account['balance']


sanjay = make_account()

ram = make_account()

# by default, when someone creates an account, balance will show 0.
putDeposit(sanjay, 5000)

# what is sanjay's balance amount now?
print("Sanjay has " + str(checkBalance(sanjay)) + " in his account!")

print("Sanjay has withdrawn 2500 rs from the account, therefore the remaining balance is " + str(withdrawMoney(sanjay, 2500)))



