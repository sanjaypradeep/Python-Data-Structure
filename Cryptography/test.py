# Enhanced Fernet Encryption Example

from cryptography.fernet import Fernet

def generate_key():
    """Generate and return a Fernet key."""
    return Fernet.generate_key()

def save_key(key, filename):
    """Save the key to a file."""
    with open(filename, 'wb') as file:
        file.write(key)

def load_key(filename):
    """Load the key from a file."""
    with open(filename, 'rb') as file:
        return file.read()

def encrypt_message(message, key):
    """Encrypt a message using the provided key."""
    f = Fernet(key)
    return f.encrypt(message.encode())

def decrypt_message(token, key):
    """Decrypt a token using the provided key."""
    f = Fernet(key)
    return f.decrypt(token).decode()

if __name__ == "__main__":
    msg = "D$bd1@k3"
    key_file = "fernet.key"

    # Generate and save key
    key = generate_key()
    print("\nGenerated Key:", key.decode())
    save_key(key, key_file)
    print("Key saved to", key_file)

    # Load key (simulating a new session)
    loaded_key = load_key(key_file)
    print("Loaded Key:", loaded_key.decode())

    # Encrypt message
    try:
        encrypted = encrypt_message(msg, loaded_key)
        print("\nEncrypted Message:", encrypted.decode())
        print("Encrypted message length:", len(encrypted))
    except Exception as e:
        print("Encryption error:", e)

    # Decrypt message
    try:
        decrypted = decrypt_message(encrypted, loaded_key)
        print("\nDecrypted Message:", decrypted)
    except Exception as e:
        print("Decryption error:", e)