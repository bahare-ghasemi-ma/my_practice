from tkinter import messagebox
from tkinter import *
import webbrowser
import pyperclip
import random
import os

root = Tk()
root.title('Contact Book')
root.geometry('650x300')
background = '#121212'
root.config(bg=background)

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()

    if not name or not phone:
        messagebox.showerror("Error", "Please enter name and phone number.")
        return

    if name.isdigit():
        messagebox.showerror("Error", "Please enter a valid name.")
        return
    
    if not phone.isdigit():
        messagebox.showerror("Error", "Please enter a valid phone number.")
        return

    contact_string = f"{name}: {phone}"
    listbox.insert(END, contact_string)
    
    name_entry.delete(0, END)
    phone_entry.delete(0, END)

def edit_contact():
    try:
        selected_contact = listbox.get(ANCHOR)
        name, phone = selected_contact.split(': ')
        
        name_entry.insert(END, name)
        phone_entry.insert(END, phone)
        listbox.delete(ANCHOR)
    except ValueError:
        messagebox.showerror("Error", "Please select a contact to edit.")

def delete_contact():
    listbox.delete(ANCHOR)

def save_list():
    with open('F:\\Django_projects\\phone_note\\save.txt', 'w', encoding='utf-8') as f:
        list_tuple = listbox.get(0, END)
        for item in list_tuple:
            f.write(item + '\n')

def open_list():
    with open('F:\\Django_projects\\phone_note\\save.txt', 'r', encoding='utf-8') as f:
        for line in f:
            listbox.insert(END, line.strip())

def open_dir():
    webbrowser.open('F:\\Django_projects\\phone_note')

def copy_number():
    try:
        selected_contact = listbox.get(ANCHOR)
        number = selected_contact.split(': ')[1]
        pyperclip.copy(number.replace('\n', ""))
    except IndexError:
        messagebox.showerror("Error", "Please select a valid contact.")

def exit_app():
    choice = messagebox.askquestion('Exit Application', 'Are you sure you want to close the application?')
    if choice == 'yes':
        root.destroy()

# Contact Name Label And Entry
name_label = Label(root, text='Contact Name:', bg=background, fg='white', font=('Calibri', 12), anchor='w', justify=LEFT)
name_label.place(relx=0.1, rely=0.1, anchor='c')

name_entry = Entry(root, bg='white', fg=background, width=30, borderwidth=2)
name_entry.place(relx=0.4, rely=0.1, anchor='c')

# Contact Number Label And Entry
phone_label = Label(root, text='   Contact Number:', bg=background, fg='white', font=('Calibri', 12), anchor='w', justify=LEFT)
phone_label.place(relx=0.1, rely=0.2, anchor='c')

phone_entry = Entry(root, bg='white', fg=background, width=30, borderwidth=2)
phone_entry.place(relx=0.4, rely=0.2, anchor='c')

# Add Contact Button
add_btn = Button(root, text='Add Contact', bg='#121212', fg='white', borderwidth=3, padx=125, command=add_contact)
add_btn.place(relx=0.29, rely=0.35, anchor='c')

# Edit Contact Button
edit_btn = Button(root, text='Edit Contact', bg='#121212', fg='white', borderwidth=3, padx=125, command=edit_contact)
edit_btn.place(relx=0.29, rely=0.45, anchor='c')

# Save List Button
save_btn = Button(root, text='Save List', bg='#121212', fg='white', borderwidth=3, padx=125, command=save_list)
save_btn.place(relx=0.29, rely=0.55, anchor='c')

# Copy Phone Number Button
copyPhone = Button(root, text='Copy Phone Number', bg=background, fg='white', borderwidth=3, padx=10, command=copy_number)
copyPhone.place(relx=0.15, rely=0.65, anchor='c')

# Delete Contact Button
deletePhone = Button(root, text='Delete Contact', bg=background, fg='white', borderwidth=3, padx=25, command=delete_contact)
deletePhone.place(relx=0.15, rely=0.77, anchor='c')

# Open Saved File Button
openSaved = Button(root, text='Open Saved File', bg=background, fg='white', borderwidth=3, padx=30, command=open_dir)
openSaved.place(relx=0.42, rely=0.65, anchor='c')

# Exit App Button
exit_btn = Button(root, text='Exit App', bg=background, fg='white', borderwidth=3, padx=50, command=exit_app)
exit_btn.place(relx=0.42, rely=0.77, anchor='c')

# List Box For Contacts
listbox = Listbox(root, width=40, height=15)
listbox.place(relx=0.75, rely=0.47, anchor='c')

open_list()
root.mainloop()