from tkinter import *
from tkinter import messagebox
import string
from random import choice,randint,shuffle
import pyperclip
import json

##------------------------ CYPHER ------------------------###


##------------------------ PASSWORD MANAGER ------------------------###

numbers = ["0","1","2","3","4","5","6","7","8","9"]
alphabet = list(string.ascii_letters )
special_characters = list(string.punctuation)

#--------------GENERATE RANDOM PASSWORD ---------#
def generate_password():
    password_entry.delete(0,END)
    password_letters = [choice(alphabet) for _ in range(randint(8,10))]
    password_numbers = [choice(numbers) for _ in range(randint(2,4))]
    password_symbols = [choice(special_characters) for _ in range(randint(2,4))]
    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)
    password_string = "".join(password_list)
    password_entry.insert(0,password_string)
    pyperclip.copy(password_string)


#-------- CREATE TXT FILE ------------#

def add_to_file():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password":password,
        }
    }
    if  len(website) == 0 or len(password) == 0:
        messagebox.showinfo(message="Make sure you have filled all the fields")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except (FileNotFoundError, json.JSONDecodeError):
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
                messagebox.showinfo(message="Your data is successfully saved")
        else:
                data.update(new_data)

                with open("data.json", "w") as data_file:
                    json.dump(data,data_file,indent=4)
                messagebox.showinfo(message="Your data is successfully saved")
        finally:
                website_entry.delete(0,END)
                password_entry.delete(0,END)

#------------- SEARCH FILE ----------#

def search_file():
    website_name = website_entry.get()
    with open("data.json","r") as data_file:
        data = json.load(data_file)
    if website_name in data:
        email_found = data[website_name]["email"]
        password_found = data[website_name]["password"]
        messagebox.showinfo(message=f"Website:{website_name}, Email: {email_found}"
                                               f"Password: {password_found}")
    else:
        messagebox.showinfo(message="Entry not found")


#--------------- GUI------------------#

window = Tk()
window.title("Password Manager")
window.config(pady=30,padx=30,bg="white")
canvas = Canvas(width=300,height=300,bg="white",highlightthickness=0)
logo_photo = PhotoImage(file="new_logo_1.png")
canvas.create_image(160,140,image=logo_photo)
canvas.grid(column=1,row=0)

#LABELS
intro_label = Label(text="Welcome to Vault-Tec's \nPassword Manager",font=("Century Gothic", 18,"bold"),bg="white",fg="dark blue")
intro_label.grid(column=1,row=1,sticky="EW",padx=10,pady=10)
website_label = Label(text="Website:",bg="white")
website_label.grid(row=2)
email_label = Label(text="Email/Username:",bg="white")
email_label.grid(row=3)
password_label = Label(text="Password",bg="white")
password_label.grid(row=4)

#ENTRY BOXES
website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(column=1,row=2,sticky="EW")
email_entry = Entry(width=35)
email_entry.grid(column=1,row=3,columnspan=2,sticky="EW")
password_entry = Entry(width=21)
password_entry.grid(column=1,row=4,sticky="EW")

#BUTTONS
generate_button = Button(text="Generate Password",command=generate_password)
generate_button.grid(column=2,row=4)
add_button = Button(text="Add", width=36, command=add_to_file)
add_button.grid(column=1,row=5,columnspan=2,sticky="EW")
search_button = Button(text="Search", command=search_file)
search_button.grid(column=2,row=2,sticky="EW")

window.mainloop()