import tkinter as tk
import random
import string

def generate_password():
    password_length = int(length_input.get())
    if password_length < 6:
        password_label.config(text="Password length should be at least 6")
    else:
        password = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(password_length))
        password_label.config(text="Generated Password: " + password)

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")
root.configure(bg="#f0f0f0")

def change_color():
    color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
    root.configure(bg=color)
    generate_button.configure(bg=color)
    length_input.configure(bg=color)
    change_color_button.configure(bg=color)
    password_label.configure(bg=color)

change_color_button = tk.Button(root, text="Change Color", command=change_color, bg="#ffb3ba", fg="black", font=("Arial", 12))
change_color_button.pack(pady=10)

label = tk.Label(root, text="Password Length:", bg="#f0f0f0", font=("Arial", 12))
label.pack()

length_input = tk.Entry(root, font=("Arial", 12))
length_input.pack()

label_complexity = tk.Label(root, text="Select Complexity:", bg="#f0f0f0", font=("Arial", 12))
label_complexity.pack()

var = tk.IntVar()
var.set(1)

complexity_options = [
    ("Easy", 1),
    ("Medium", 2),
    ("Hard", 3)
]

for text, mode in complexity_options:
    complexity_button = tk.Radiobutton(root, text=text, variable=var, value=mode, bg="#f0f0f0", font=("Arial", 10))
    complexity_button.pack()

def generate_password():
    password_length = int(length_input.get())
    complexity_mode = var.get()
    if password_length < 6:
        password_label.config(text="Password length should be at least 6")
    else:
        if complexity_mode == 1:
            characters = string.ascii_letters + string.digits
        elif complexity_mode == 2:
            characters = string.ascii_letters + string.digits + string.punctuation
        else:
            characters = string.ascii_letters + string.digits + string.punctuation + string.ascii_uppercase + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(password_length))
        password_label.config(text="Generated Password: " + password)

generate_button = tk.Button(root, text="Generate Password", command=generate_password, bg="#90ee90", font=("Arial", 12))
generate_button.pack(pady=10)

password_label = tk.Label(root, text="", bg="#f0f0f0", font=("Arial", 12), wraplength=300)
password_label.pack()

root.mainloop()
