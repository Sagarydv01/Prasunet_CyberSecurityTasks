"""
TASK-03: PASSWORD COMPLEXITY CHECKER

Build a tool that assesses the strength of a password based on criteria such as length, presence of uppercase and lowercase letters, numbers, and special characters. Provide feedback to users on the password's strength.
"""

import tkinter as tk
from tkinter import *
import string

def is_sequential(password):
    sequences = [string.ascii_lowercase, string.ascii_uppercase, string.digits]
    for seq in sequences:
        for i in range(len(seq) - 2):
            sub_seq = seq[i:i + 3]
            if sub_seq in password or sub_seq[::-1] in password:
                return True
    return False

def check_password():
    password = password_entry.get()

    strength = 0
    remarks = []

    if len(password) < 8:
        remarks.append("Password should be at least 8 characters long.")
    else:
        strength += 1
    
    if any(char.islower() for char in password):
        strength += 1
    else:
        remarks.append("Include at least one lowercase letter.")
    
    if any(char.isupper() for char in password):
        strength += 1
    else:
        remarks.append("Include at least one uppercase letter.")
    
    if any(char.isdigit() for char in password):
        strength += 1
    else:
        remarks.append("Include at least one numeric digit.")
    
    if any(char in string.punctuation for char in password):
        strength += 1
    else:
        remarks.append("Include at least one special character.")

    if is_sequential(password):
        remarks.append("Password should not contain sequences of numbers or letters (e.g., '123', 'abc').")
        strength = min(strength, 2)  # Reduce strength to weak if sequence is found

    if strength == 5:
        result_text.set("Very Strong Password")
    elif strength == 4:
        result_text.set("Strong Password")
    elif strength == 3:
        result_text.set("Moderate Password")
    elif strength == 2:
        result_text.set("Weak Password")
    else:
        result_text.set("Very Weak Password")

    if remarks:
        remarks_text.set("\n".join(remarks))
    else:
        remarks_text.set("")

def clear_entries():
    password_entry.delete(0, tk.END)
    result_text.set("")
    remarks_text.set("")

root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("350x400")

title_label = tk.Label(root, text="Password Strength Checker", font=("Arial", 18, "bold"))
title_label.pack(pady=10)

password_label = tk.Label(root, text="Enter Password:", font=("Arial", 12))
password_label.pack()

password_entry = tk.Entry(root, show='*', font=("Arial", 12))
password_entry.pack(pady=5)

check_button = tk.Button(root, text="Check Password", command=check_password, font=("Arial", 12))
check_button.pack(pady=10)

result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, font=("Arial", 14, "bold"), fg="blue")
result_label.pack(pady=10)

remarks_text = tk.StringVar()
remarks_label = tk.Label(root, textvariable=remarks_text, font=("Arial", 12), wraplength=300, justify="left", fg="red")
remarks_label.pack(pady=10)

clear_button = tk.Button(root, text="Clear", command=clear_entries, font=("Arial", 12))
clear_button.pack(pady=5)

root.mainloop()

#                                       Task Completed!