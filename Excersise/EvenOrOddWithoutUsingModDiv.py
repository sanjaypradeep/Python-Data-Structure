__author__ = 'Sanjay'

# The below program is to check whether the given number is odd or even
# The logic is acheived by Bit wise operator
# normally people will use Modulo or division operator to find its even or odd.

numList = range(0, 10, 2)  # [0,2,4,6,8]

def commonLogicPlusMyOwnImplementation(n):
    # used bit wise operator logic and also checking whether the last number of the digit
    # is there in numList, which is a common declared list at the top
    if ((n & 1 == 0) or (n in numList)):
        print("It's a Even Number")
    else:
        print("It's a Odd Number")
if __name__ == '__main__':
    try:
        getIn = raw_input("Please give a input to check whether the number is even or odd")
        if getIn.isdigit(): # checks whether the user given input is valid or not.
            if getIn == 1 or getIn >1:
                commonLogicPlusMyOwnImplementation(int(getIn))
        else:
            raise ArithmeticError("Something is wrong in the given input!Check it.")
    except ArithmeticError as e:
        print(e.message)
    else:
        print("Thanks for testing me!")