def encrypt(key, msg):
    encryptedText = []
    for i, c in enumerate(msg):
        key_c = ord(key[i % len(key)])
        msg_c = ord(c)
        encryptedText.append(chr((msg_c + key_c) % 3691))
    return ''.join(encryptedText)

def decrypt(key, encryptedText):
    msg = []
    for i, c in enumerate(encryptedText):
        key_c = ord(key[i % len(key)])
        enc_c = ord(c)
        msg.append(chr((enc_c - key_c) % 3691))
    return ''.join(msg)

if __name__ == '__main__':
    key = 'MyAwesome_FirstProgram_ForEncryption_GoodJob'
    msg = "Hello world, Hope you're doing awesome!"
    encrypted = encrypt(key, msg)
    decrypted = decrypt(key, encrypted)

    print 'Message:', repr(msg)
    print 'Key:', repr(key)
    print 'Encrypted:', repr(encrypted)
    print 'Decrypted:', repr(decrypted)