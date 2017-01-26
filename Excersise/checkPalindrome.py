def checkPalindrome():
    userInput = input("Enger a string or integer")
    try:
        if type(userInput) is str:
            if userInput == userInput[::-1]:
                print ('its a palindrome')
            else:
                raise Exception
        else:
            print ("is it something else?")
    except Exception as e:
        print (e)


if __name__ == '__main__':
     checkPalindrome()
