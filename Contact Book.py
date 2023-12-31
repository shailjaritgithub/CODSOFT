import tkinter as tk
from tkinter import messagebox

# Sample initial contacts
contacts = [
    {"name": "John Doe", "phone": "1234567890", "email": "john@example.com", "address": "123 Main St"},
    {"name": "Riya Rojha", "phone": "9876543210", "email": "jane@example.com", "address": "456 Elm St"},
    {"name": "Freddy Mark", "phone": "222267890", "email": "john@example.com", "address": "123 Main St"},
    {"name": "Sam Gomes", "phone": "8888777543210", "email": "jane@example.com", "address": "456 Elm St"}
]

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if name and phone:  # Check if name and phone are provided
        contacts.append({"name": name, "phone": phone, "email": email, "address": address})
        messagebox.showinfo("Success", "Contact added successfully!")
        clear_entries()
    else:
        messagebox.showerror("Error", "Name and Phone are required fields.")

def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

def view_contacts():
    contact_list.delete(0, tk.END)
    for contact in contacts:
        contact_list.insert(tk.END, f"{contact['name']} - {contact['phone']}")

def search_contact():
    search_term = search_entry.get()
    contact_list.delete(0, tk.END)
    for contact in contacts:
        if search_term.lower() in contact['name'].lower() or search_term in contact['phone']:
            contact_list.insert(tk.END, f"{contact['name']} - {contact['phone']}")

def delete_contact():
    selected_contact = contact_list.curselection()
    if selected_contact:
        index = selected_contact[0]
        del contacts[index]
        view_contacts()
        messagebox.showinfo("Success", "Contact deleted successfully!")
    else:
        messagebox.showerror("Error", "Please select a contact to delete.")

def update_contact():
    selected_contact = contact_list.curselection()
    if selected_contact:
        index = selected_contact[0]
        name = name_entry.get()
        phone = phone_entry.get()
        email = email_entry.get()
        address = address_entry.get()

        if name and phone:
            contacts[index] = {"name": name, "phone": phone, "email": email, "address": address}
            view_contacts()
            messagebox.showinfo("Success", "Contact updated successfully!")
        else:
            messagebox.showerror("Error", "Name and Phone are required fields.")
    else:
        messagebox.showerror("Error", "Please select a contact to update.")

root = tk.Tk()
root.title("Contact Book")

# Styling
root.configure(bg='pink')
title_font = ("Helvetica", 16, "bold")
button_font = ("Helvetica", 10)
label_font = ("Helvetica", 10)
entry_bg = "light yellow"

# Labels
tk.Label(root, text="Name:", font=label_font, bg=root.cget('bg')).grid(row=0, column=0, sticky="w", pady=5)
tk.Label(root, text="Phone:", font=label_font, bg=root.cget('bg')).grid(row=1, column=0, sticky="w", pady=5)
tk.Label(root, text="Email:", font=label_font, bg=root.cget('bg')).grid(row=2, column=0, sticky="w", pady=5)
tk.Label(root, text="Address:", font=label_font, bg=root.cget('bg')).grid(row=3, column=0, sticky="w", pady=5)

# Entries
name_entry = tk.Entry(root, bg=entry_bg)
name_entry.grid(row=0, column=1, pady=5)
phone_entry = tk.Entry(root, bg=entry_bg)
phone_entry.grid(row=1, column=1, pady=5)
email_entry = tk.Entry(root, bg=entry_bg)
email_entry.grid(row=2, column=1, pady=5)
address_entry = tk.Entry(root, bg=entry_bg)
address_entry.grid(row=3, column=1, pady=5)

# Buttons
add_button = tk.Button(root, text="Add Contact", bg="#20B2AA", font=button_font, command=add_contact)
add_button.grid(row=4, column=0, columnspan=2, pady=10)
view_button = tk.Button(root, text="View Contacts", bg="#20B2AA", font=button_font, command=view_contacts)
view_button.grid(row=5, column=0, columnspan=2, pady=5)
search_button = tk.Button(root, text="Search",bg="#20B2AA", font=button_font, command=search_contact)
search_button.grid(row=6, column=0, pady=5)
delete_button = tk.Button(root, text="Delete Contact", bg="#20B2AA", font=button_font, command=delete_contact)
delete_button.grid(row=6, column=1, pady=5)
update_button = tk.Button(root, text="Update Contact", bg="#20B2AA", font=button_font, command=update_contact)
update_button.grid(row=7, column=0, columnspan=2, pady=5)

# Search Entry
search_entry = tk.Entry(root, bg=entry_bg)
search_entry.grid(row=8, column=0, columnspan=2, pady=5)

# Contact List
contact_list = tk.Listbox(root, width=40, font=label_font, bg=entry_bg)
contact_list.grid(row=9, column=0, columnspan=2, pady=5)

root.mainloop()
