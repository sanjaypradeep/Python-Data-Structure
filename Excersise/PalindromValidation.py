
# Not checking for Special characters.
def checkPalindrome():
    userInput = input("Enter a string or integer")
    try:
        if type(userInput) is str or type(userInput) is int:
            if userInput == userInput[::-1]:
                print ('its a palindrome')
            else:
                raise Exception("It's not a palindrom, better luck next time")
        else:
            print ("is it something else?Please check.")
    except Exception as e:
        print (e.message)
        

if __name__ == '__main__':
     checkPalindrome()
