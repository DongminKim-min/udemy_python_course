from tkinter import *
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_data():
    website = website_entry.get()
    user = user_entry.get()
    password = password_entry.get()

    is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {user} "
                                                  f"\nPassword: {password} \nIs it okay to save?")

    if is_ok:
        with open("data_file.txt", mode="a") as file:
            file.write(f"{website} | {user} | {password}\n")
            website_entry.delete(first=0, last="end")
            password_entry.delete(first=0, last="end")




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
website_entry = Entry(width=40)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
user_entry = Entry(width=40)
user_entry.grid(row=2, column=1, columnspan=2)
user_entry.insert(0, "dave012284@gmail.com")
password_entry = Entry(width=24)
password_entry.grid(row=3, column=1)

#Button
generate_button = Button(text="Generate Password", width=15)
generate_button.grid(row=3, column=2)
add_button = Button(text="Add", width=40, command=add_data)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()