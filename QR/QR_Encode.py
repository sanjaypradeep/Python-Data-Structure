
# Hey in this file, we are going to explore about QR Code.

# Now a days, it's common to people are scanning the QR Code in any shopping mall for the payment. 
# In general, when you scan the code via QR Code Scanner/Reader - internally it reads the data in the code and do action accordingly.

# Let's how to create/make a QR code - which internally has some text or data.

# We'll be writing a program - Takes input from the user, construct a QR code in .png format - output of this execution should bring a QR code (which user data will be binding internally)

# Using a Python Library called ```pyqrcode```

# Here's the steps for installing that library,

# Windows
# 1. pip install pyqrcode
# 2. pip install pypng


import pyqrcode

# firstLevelQRCode = pyqrcode.create("Hello World") # Hello world is the text which I'm appending to generate a QR Code.

# when you try printing the img variable - QRCode(content=b'Hello World', error='H', version=2, mode='binary')
# means it gives QRCode object 

# print(type(firstLevelQRCode)) - <class 'pyqrcode.QRCode'>

# finalImage = firstLevelQRCode.png("HelloWorldQR.png", scale=6) # 

# print("Output would have generated")

def takeInputFromUser():
    givenInput = input("Enter the data : ")
    if givenInput:
        print("As an output, you can expect a QR Code in .png format")
        return givenInput
    else:
        print("Please input some data")
        return None   

def getFileNameFromUser():
    import random
    fileName = input("Enter the filename: ")
    return fileName if fileName else str(random.randint(1,100))

def constructQR():
    infoFromUser = takeInputFromUser()
    if(infoFromUser):
        output = pyqrcode.create(infoFromUser)
        fileName = getFileNameFromUser()
        output.png(fileName + '.png', scale=6)
        print(fileName + ".png file got generated and saved in your local.")
    else:
        takeInputFromUser()    
    
if __name__ == '__main__':
    constructQR()