from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    list1 = [password_list.append(random.choice(letters)) for _ in range(nr_letters)]
    list2 = [password_list.append(random.choice(symbols)) for _ in range(nr_symbols)]
    list3 = [password_list.append(random.choice(numbers)) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_website_data():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    new_data = {website: {
        "email": email,
        "password": password
    }}

    if len(website) == 2 or len(password) == 2:
        messagebox.showinfo(title="Error", message="Error! Either website or password length is too short.")
    else:
        try:
            with open("saved_passwords.json", "r") as website_data:
                # Data loaded
                data = json.load(website_data)

        except FileNotFoundError:
            with open("saved_passwords.json", "w") as website_data:
                json.dump(new_data, website_data, indent=4)

        # Else block will be triggered, if everything in the try block succeeds
        else:
            # Update dictionary with some new piece of data
            data.update(new_data)

            with open("saved_passwords.json", "w") as website_data:
                # Save updated data
                json.dump(data, website_data, indent=4)

        finally:
            website_input.delete("0", "end")
            password_input.delete("0", "end")


# ---------------------------- SEARCH FUNCTION ------------------------------- #

def find_password():
    user_website = website_input.get().title()

    try:
        with open("saved_passwords.json", "r") as website_data:
            data = json.load(website_data)

    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")

    else:
        if user_website in data:
            password_find = data[user_website]['password']
            email_find = data[user_website]['email']
            messagebox.showinfo(title=user_website, message=f"Email: {email_find}\nPassword: {password_find}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for the {user_website} exists.")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=20)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.config()
canvas.grid(column=1, row=0)

website = Label(text="Website")
website.grid(column=0, row=1)

email = Label(text="Email/Username:")
email.grid(column=0, row=2)

password = Label(text="Password")
password.grid(column=0, row=3, sticky=W)

website_input = Entry(width=32)
website_input.grid(column=1, row=1)
website_input.focus()

search_button = Button(text="Search", width=14, command=find_password)
search_button.grid(column=2, row=1)

email_input = Entry(width=50)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "rene@rene.ee")

password_input = Entry(width=32)
password_input.grid(column=1, row=3)

generate_pass = Button(text="Generate Password", command=password_generator)
generate_pass.grid(column=2, row=3)

add_button = Button(text="Add", width=43, command=save_website_data)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
