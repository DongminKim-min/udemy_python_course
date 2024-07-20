from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list) #list, dict, tuple -> string으로 join / 사이에 "?" 끼워 넣을 수 있음
    password_entry.insert(0, password)

    '''pyperclip -> copy the password automatically'''
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_data():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if website == "" or password == "":
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty")
    else:
        try:
            with open("data.json", mode="r") as data_file: # json file 없으면 자동으로 생성
                #Reading old data
                data = json.load(data_file)

        #If there's no data.json
        except FileNotFoundError:
            with open("data.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", mode="w") as data_file:
                #Saving updated data
                json.dump(data, data_file, indent=4)

        finally:
            website_entry.delete(first=0, last="end")
            password_entry.delete(first=0, last="end")

# -------------------------------SEARCH-------------------------------- #
def find_password():
    try:
        with open("data.json", mode="r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Oops", message="No Data File Found.")
    else:
        if website_entry.get() in data:
            website_info = data[website_entry.get()]
            email = website_info["email"]
            password = website_info["password"]
            messagebox.showinfo(title=f"{website_entry.get()}",
                                message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Oops", message="No details for the website exists.")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady= 50)

img_file = PhotoImage(file= "logo.png")
canvas = Canvas(height=200, width=200)
canvas.create_image(100, 100, image=img_file)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
user_label = Label(text= "Email/Username:")
user_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width=24)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = Entry(width=43)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "dave012284@gmail.com")
password_entry = Entry(width=24)
password_entry.grid(row=3, column=1)

#Button
generate_button = Button(text="Generate Password", width=15, command=generate_password)
generate_button.grid(row=3, column=2)
add_button = Button(text="Add", width=37, command=add_data)
add_button.grid(row=4, column=1, columnspan=2)
search_button = Button(text="Search", width=15, command=find_password)
search_button.grid(row=1, column=2)

window.mainloop()