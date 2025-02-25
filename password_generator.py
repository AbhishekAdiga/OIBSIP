#Password Generater with GUI
import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password():
    try:
        length = int(length_entry.get())
        use_letters = letters_var.get()
        use_numbers = numbers_var.get()
        use_symbols = symbols_var.get()

        characters = ""

        if use_letters:
            characters += string.ascii_letters
        if use_numbers:
            characters += string.digits
        if use_symbols:
            characters += string.punctuation

        if not characters:
            messagebox.showerror("Error", "Please select at least one character type!")
            return
        
        password = ''.join(random.choice(characters) for _ in range(length))

        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid password length!")

# Function to copy password to clipboard
def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(password_entry.get())
    root.update()
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# GUI Setup
root = tk.Tk()
root.title("Random Password Generator")
root.geometry("400x300")
root.resizable(False, False)

# UI Elements
tk.Label(root, text="Password Length:").pack(pady=5)
length_entry = tk.Entry(root)
length_entry.pack(pady=5)
length_entry.insert(0, "12")  # Default length

letters_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Include Letters", variable=letters_var).pack()
tk.Checkbutton(root, text="Include Numbers", variable=numbers_var).pack()
tk.Checkbutton(root, text="Include Symbols", variable=symbols_var).pack()

generate_btn = tk.Button(root, text="Generate Password", command=generate_password)
generate_btn.pack(pady=10)

password_entry = tk.Entry(root, width=30)
password_entry.pack(pady=5)

copy_btn = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_btn.pack(pady=10)

root.mainloop()





# Basic Password Generator
# import random
# import string

# def generate_password(length_l,inc_str,inc_num,inc_symbols):

#     character = ""

#     if inc_str == True:
#         character += string.ascii_letters
#     if inc_num == True:
#         character += string.digits
#     if inc_symbols == True:
#         character += string.punctuation

#     if not character:
#         return "Error: Select at least one character type"
    
#     return ("".join(random.choice(character) for _ in range(length_l))) # joins(random elements from charecter's selected in the range of given length)

# #input
# length_l = int(input("Enter the length of password to be genreated : "))
# inc_str = input("Do you want to include string's/charecters? (yes/no)").lower() == "yes"
# inc_num = input("Do you want to include numbers? (yes/no)").lower() == "yes"
# inc_symbols = input("Do you want to include symbols? (yes/no)").lower() == "yes"

# password = generate_password(length_l,inc_str,inc_num,inc_symbols)

# print(f"Password Generated: {password}")