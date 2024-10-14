# Basic Fernet

# msg = "I am going to encrypt this sentence using Fernet"
msg = "D$bd1@k3"

from cryptography import fernet
from cryptography.fernet import Fernet

# first generate key
eKey = Fernet.generate_key()
print("\nKey is : " + eKey.decode())
# print("\nType of key is .. " + str(type(eKey)))
print("\nKey is : " + str(len(eKey.decode())))

# create a class instance object
f1 = Fernet(eKey)

eMsg = f1.encrypt(msg.encode()) # f1 instance can encrypt only bytes
print("\nEncrypted message is - " + eMsg.decode())
print("\nEncrypted message is -" + str(len(eMsg)))

# decrypt with same instance
dMsg = f1.decrypt(eMsg).decode()
print("\nDecrypted Message - " + dMsg)