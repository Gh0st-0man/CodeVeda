import os
from cryptography.fernet import Fernet

def generate_key():
    """Generates a key and saves it into a file."""
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("Key generated and saved as 'secret.key'. Keep this safe!")

def load_key():
    """Loads the key from the current directory."""
    try:
        return open("secret.key", "rb").read()
    except FileNotFoundError:
        print("Error: 'secret.key' not found. Please generate a key first.")
        return None

def encrypt_file(filename):
    """Encrypts the file and adds .encrypted extension."""
    key = load_key()
    if not key: return

    fernet = Fernet(key)
    
    try:
        with open(filename, "rb") as file:
            file_data = file.read()
        
        encrypted_data = fernet.encrypt(file_data)
        
        new_filename = filename + ".encrypted"
        with open(new_filename, "wb") as file:
            file.write(encrypted_data)
            
        print(f"Success! Encrypted file saved as: {new_filename}")
        
    except FileNotFoundError:
        print("Error: The file you specified does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

def decrypt_file(filename):
    """Decrypts the file and removes the .encrypted extension."""
    key = load_key()
    if not key: return

    fernet = Fernet(key)
    
    try:
        with open(filename, "rb") as file:
            encrypted_data = file.read()
        
        decrypted_data = fernet.decrypt(encrypted_data)
        
        # Remove .encrypted extension if present, otherwise add .decrypted
        if filename.endswith(".encrypted"):
            new_filename = filename[:-10] # Removes last 10 chars
        else:
            new_filename = "decrypted_" + filename

        with open(new_filename, "wb") as file:
            file.write(decrypted_data)
            
        print(f"Success! Decrypted file saved as: {new_filename}")

    except  FileNotFoundError:
        print("Error: The file you specified does not exist.")
    except Exception:
        print("Error: Decryption failed. Wrong key or corrupted file.")

def main():
    while True:
        print("\n--- File Encryption Tool ---")
        print("1. Generate Key")
        print("2. Encrypt a File")
        print("3. Decrypt a File")
        print("4. Exit")
        
        choice = input("Select an option (1-4): ")

        if choice == '1':
            generate_key()
        elif choice == '2':
            filename = input("Enter the filename to encrypt (e.g., data.txt): ")
            encrypt_file(filename)
        elif choice == '3':
            filename = input("Enter the filename to decrypt (e.g., data.txt.encrypted): ")
            decrypt_file(filename)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid selection.")

if __name__ == "__main__":
    main()