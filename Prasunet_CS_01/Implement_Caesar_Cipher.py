""" Task 01: Implement Caesar Cipher
Create a Python program that can encrypt and decrypt text using the Caesar Cipher algorithm. 
Allow users to input a message and a shift value to perform encryption and decryption. """

import tkinter as tk
from tkinter import messagebox

def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) + shift - 65) % 26 + 65)
            else:
                result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

def decrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - shift - 65) % 26 + 65)
            else:
                result += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            result += char
    return result

def perform_encryption():
    try:
        text = text_entry.get()
        shift = int(shift_entry.get())
        encrypted_text = encrypt(text, shift)
        result_label.config(text=f"Encrypted Text: {encrypted_text}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid shift value.")

def perform_decryption():
    try:
        text = text_entry.get()
        shift = int(shift_entry.get())
        decrypted_text = decrypt(text, shift)
        result_label.config(text=f"Decrypted Text: {decrypted_text}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid shift value.")

root = tk.Tk()
root.title("Caesar Cipher Tool")
root.geometry("400x300")

text_label = tk.Label(root, text="Enter Text:")
text_label.pack(pady=10)

text_entry = tk.Entry(root, width=50)
text_entry.pack(pady=5)

shift_label = tk.Label(root, text="Enter Shift Value:")
shift_label.pack(pady=10)

shift_entry = tk.Entry(root, width=10)
shift_entry.pack(pady=5)

encrypt_button = tk.Button(root, text="Encrypt", command=perform_encryption)
encrypt_button.pack(pady=10)

decrypt_button = tk.Button(root, text="Decrypt", command=perform_decryption)
decrypt_button.pack(pady=10)

result_label = tk.Label(root, text="", wraplength=300)
result_label.pack(pady=20)

root.mainloop()

# Task Completed!