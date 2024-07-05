""" Task 01: Implement Caesar Cipher
Create a Python program that can encrypt and decrypt text using the Caesar Cipher algorithm. Allow users to input a message and a shift value to perform encryption and decryption. """

def encrypt(text, shift):
    result = ""
    
    for i in range(len(text)):
        char = text[i]
        if char.isupper(): 
            result += chr((ord(char) + shift - 65) % 26 + 65)
        else:
            result += chr((ord(char) + shift - 97) % 26 + 97)
    return result

def decrypt(text, shift):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) - shift - 65) % 26 + 65)
        else:
            result += chr((ord(char) - shift - 97) % 26 + 97)
    return result


if __name__ == "__main__":
    text = input("Enter the text: ")
    shift = int(input("Enter shift value: "))
    
    encrypted_text = encrypt(text, shift)
    print(f"Encrypted Text: {encrypted_text}")
    
    decrypted_text = decrypt(encrypted_text, shift)
    print(f"Decrypted Text: {decrypted_text}")

# Task Completed!