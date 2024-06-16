from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

FONT_NAME = 'Courier'

window = Tk()
window.title('My Password Manager')
window.config(padx=60, pady=60, bg='white')

# ========================= Password Generator ==========================

def generate_password():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    
    symbols = ['@', '!', '#', '$', '%', '^', '&', '*', '(', ')', '+', '-', '/', '?', '|', '\\', ':', ';', '~', '`', '{', '}', '[', ']', '.']
    
    alpha1 = list(map(chr, range(97, 123)))
    alpha2 = list(map(chr, range(65, 91)))
    alpha = alpha1 + alpha2
    
    password_letters = [choice(alpha) for ch in range(randint(8, 10))]
    password_symbols = [choice(symbols) for sy in range(randint(2, 4))]
    password_numbers = [str(choice(numbers)) for n in range(randint(2, 4))]
     
    Password = password_letters + password_symbols + password_numbers
        
    shuffle(Password)
    
    final_password = ''.join(Password)
    
    password_input.delete(0, END)
    password_input.insert(0, final_password)
    pyperclip.copy(final_password)
    
# ======================= Find a Password ===========================

def find_password():
    website_name = website_input.get()
    try:
        with open('data.json', 'r') as data_file:
            data = json.load(data_file)
            messagebox.showinfo(title=website_name, message=f"Email: {data[website_name]['email']} \n\nPassword: {data[website_name]['password']}")
            
    except (FileNotFoundError, KeyError):
        messagebox.showinfo(title='Oops!', message=f"Sorry!, No such Entry Found.")
            
            
# ======================= Save a File ============================

def save_file():
    website_name = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website_name:{
            'email': email,
            'password': password,
        }
    }
    
    
    # Checking weather the details is empty or not:
    if (len(website_name) == 0 or len(email) == 0 or len(password) == 0):
        messagebox.askretrycancel(title='Warning!', message=f"Please donot leave any feild empty.")
        website_input.delete(0, END)
        password_input.delete(0, END)
        website_input.focus()
    
    else:
        is_ok = messagebox.askokcancel(title=website_name, message=f"Details Entered: \n\nEmail: {email} \n\nPassword: {password} \n\nIs it Okay to Save?")
    
    # Confirming entries:
        if is_ok:
            try:
                with open('data.json', 'r') as data_file:
                    # Reading old data
                    data = json.load(data_file)
            
            except FileNotFoundError:
                with open('data.json', 'w') as data_file:
                    json.dump(new_data, data_file, indent=4)
                
            else:
                data.update(new_data)
                
                with open('data.json', 'w') as data_file:
                    json.dump(data, data_file, indent=4)
                    
            finally:
                website_input.delete(0, END)
                password_input.delete(0, END)
                website_input.focus()
                
                
            is_yes = messagebox.askyesno(message=f'Details Saved Successfully!\n\nAdd another password?\n')
            
            if is_yes:
                website_input.delete(0, END)
                password_input.delete(0, END)
                website_input.focus()
    
    
# ===================== SETUP ========================

# Canvas:
canvas = Canvas(width=200, height=200, bg='white', highlightthickness=0)
img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)


# Website Name:
website_label = Label(text='Website:', font=(FONT_NAME, 10, 'bold'))
website_label.grid(column=0, row=1)
website_label.config(bg='white', highlightthickness=0)

website_input = Entry(width=24)
website_input.grid(column=1, row=1)
website_input.focus()
website_input.config(bg='white', highlightthickness=0)

# Emai/Username:
email_label = Label(text='Email/Username:', font=(FONT_NAME, 10, 'bold'))
email_label.grid(column=0, row=2)
email_label.config(bg='white', highlightthickness=0)

email_input = Entry(width=40)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, 'ansh.mn.soni@gmail.com')
email_input.config(bg='white', highlightthickness=0)


# Password:
password_label = Label(text='Password', font=(FONT_NAME, 10, 'bold'))
password_label.grid(column=0, row=3)
password_label.config(bg='white', highlightthickness=0)

password_input = Entry(width=24)
password_input.grid(column=1, row=3)
password_input.config(bg='white', highlightthickness=0)

# Generate Button:
generate = Button(text='Generate Password', command=generate_password, font=(FONT_NAME, 10, 'bold'))
generate.grid(column=2, row=3)
generate.config(padx=-15, pady=-10, bg='white', highlightthickness=0)


# Search Button:
search = Button(text='Search', command=find_password, font=(FONT_NAME, 10, 'bold'))
search.grid(column=2, row=1)
search.config(padx=45, pady=-10, bg='white', highlightthickness=0)

# Add Button:
add_button = Button(text='Add', command=save_file, width=42, font=(FONT_NAME, 10, 'bold'))
add_button.grid(column=1, row=4, columnspan=2)
add_button.config(pady=-10, bg='white', highlightthickness=0)

window.mainloop()