""" Task 2: Pixel Manipulation for Image Encryption
Develop a simple image encryption tool using pixel manipulation. 
You can perform operations like swapping pixel values or applying 
basic a mathematical operation to each pixel. 
Allow users to encrypt and decrypt images.
"""
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

root = Tk()
root.geometry("500x500")
root.title("Pixel Manipulation Image Encryption")

selected_file_path = None

def select_file():
    global selected_file_path
    selected_file_path = filedialog.askopenfilename(
        filetypes=[
            ('Image files', '*.jpg;*.png;*.bmp;*.gif')
        ]
    )
    if selected_file_path:
        file_label.config(text=f"Selected File: {selected_file_path}")
        load_image(selected_file_path)
    else:
        file_label.config(text="No file selected")

def load_image(file_path):
    image = Image.open(file_path)
    image.thumbnail((250, 250))
    img = ImageTk.PhotoImage(image)
    img_label.config(image=img)
    img_label.image = img

def manipulate_pixels(encrypt=True):
    if not selected_file_path:
        result_label.config(text="No file selected. Please select a file first.")
        return

    key = key_entry.get().strip()

    try:
        key = int(key)
    except ValueError:
        result_label.config(text="Invalid key. Please enter a valid integer.")
        return

    try:
        with Image.open(selected_file_path) as img:
            img = img.convert("RGB")
            pixels = img.load()
            width, height = img.size

            for i in range(width):
                for j in range(height):
                    r, g, b = pixels[i, j]
                    if encrypt:
                        # Encrypt: XOR operation
                        pixels[i, j] = (r ^ key, g ^ key, b ^ key)
                    else:
                        # Decrypt: Reverse XOR operation to retrieve original values
                        pixels[i, j] = (r ^ key, g ^ key, b ^ key)

            img.save(selected_file_path)
        
        load_image(selected_file_path)
        action = "encrypted" if encrypt else "decrypted"
        result_label.config(text=f"Image {action} successfully.\nFile path: {selected_file_path}, \nKey (used for Encryption/Decryption): {key}")
    except Exception as e:
        result_label.config(text=f"Error during processing: {str(e)}")

select_file_button = Button(root, text="Select File", command=select_file, width=15)
select_file_button.place(x=180, y=20)

file_label = Label(root, text="No file selected", wraplength=400)
file_label.place(x=50, y=60)

img_label = Label(root)
img_label.place(x=125, y=100)

encrypt_button = Button(root, text="ENCRYPT", command=lambda: manipulate_pixels(encrypt=True), width=15)
encrypt_button.place(x=120, y=380)

decrypt_button = Button(root, text="DECRYPT", command=lambda: manipulate_pixels(encrypt=False), width=15)
decrypt_button.place(x=260, y=380)

key_label = Label(root, text="Enter Key to Encrypt/Decrypt File:", anchor="w")
key_label.place(x=50, y=320, width=200)

key_entry = Entry(root, width=20)
key_entry.place(x=260, y=320)

result_label = Label(root, text="", wraplength=400)
result_label.place(x=50, y=420)

root.mainloop()