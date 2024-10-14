# Example 3: Using **kwargs to pass the variable keyword arguments to the function 
def intro(**data):
    print("\nData type of argument:",type(data))

    for key, value in data.items():
        print("{} is {}".format(key,value))

intro(Firstname="Sita", Lastname="Sharma", Age=22, Phone=1234567890)
intro(Firstname="John", Lastname="Wood", Email="johnwood@nomail.com", Country="Wakanda", Age=25, Phone=9876543210)
# When we run the above program, the output will be

# Data type of argument: <class 'dict'>
# Firstname is Sita
# Lastname is Sharma
# Age is 22
# Phone is 1234567890

# Data type of argument: <class 'dict'>
# Firstname is John
# Lastname is Wood
# Email is johnwood@nomail.com
# Country is Wakanda
# Age is 25
# Phone is 9876543210


# In the above program, we have a function intro() with **data as a parameter. We passed two dictionaries with variable argument length to the intro() function. We have for loop inside intro() function which works on the data of passed dictionary and prints the value of the dictionary.

'''
Things to Remember:
1. *args and *kwargs are special keyword which allows function to take variable length argument.
2. *args passes variable number of non-keyworded arguments list and on which operation of the list can be performed.
3. **kwargs passes variable number of keyword arguments dictionary to function on which operation of a dictionary can be performed.
4. *args and **kwargs make the function flexible.
'''