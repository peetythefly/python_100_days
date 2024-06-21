from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
LETTERS = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
NUMBERS = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
SYMBOLS = ('!', '#', '$', '%', '&', '(', ')', '*', '+')

# ---------------------------- SEARCH FOR PASSWORD ------------------------------- #
def search_pass():
    # Get the user search string.
    srch_str = web_entry.get()
    # Get the file data. Exception on if the file is empty.
    try:
        with open(file="secret_data.json", mode="r") as secret_file:
            # Read old data.
            secret_data = json.load(secret_file)
    except: 
        print("File not found. Creating it now.")
        # We create an empty file and set the secret data to empty.
        with open(file="secret_data.json", mode="w") as secret_file:
            json.dump({}, secret_file, indent=4)
        secret_data = {}

    if srch_str in secret_data:
        email = secret_data[srch_str]["email"]
        psswd = secret_data[srch_str]["password"]
        # Clear the entries then input the new data.
        user_entry.delete(0, END)
        pass_entry.delete(0, END)
        user_entry.insert (0, email)
        pass_entry.insert (0, psswd)
    else:
        messagebox.showinfo(message="No Website exists with that name.")
    
    

            


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_pass():
    # We want a 12 character password. 
    password = ""
    nr_symbols = random.randint(2,4)
    nr_numbers = random.randint(2,4)
    nr_letters = 12 - (nr_symbols + nr_numbers)
    while (nr_letters + nr_numbers + nr_symbols) > 0:
        # Uncomment this to see the logic worked out as each character is added.

        # Randomly select whether to add a letter, symbol, or number next. 
        # 0 - letter, 1 - number, 2 - symbol.
        # This makes it more efficient. We can cut out nr_letters or nr_numbers and then we will go through the loop fewer times.
        if nr_letters == 0:
            choice = random.randint (1, 2)
        elif nr_symbols == 0:
            choice = random.randint (0, 1)
        else:
            choice = random.randint (0, 2)
        # Add a letter only if there are letters left to add.
        if choice == 0 and nr_letters > 0:
            password += LETTERS[random.randint (0, len (LETTERS) - 1)]
            nr_letters -= 1
        elif choice == 1 and nr_numbers > 0:
            password += NUMBERS[random.randint (0, len (NUMBERS) - 1)]
            nr_numbers -= 1
        elif choice == 2 and nr_symbols > 0:
            password += SYMBOLS[random.randint (0, len (SYMBOLS) - 1)]
            nr_symbols -= 1
    # Add the generated password into the password box.
    pass_entry.insert(0, password)
    # Copy the password to the clipboard.
    messagebox.showinfo(title="Notify", message="Password copied to your clipboard.")
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_pass():
    site_text = web_entry.get()
    email_text = user_entry.get()
    pass_text = pass_entry.get()
    json_data = {
        site_text: {
            "email": email_text,
            "password": pass_text,
        }}
    # messagebox.showinfo(title="Notification", message="Password saved.")
    ok_to_save = messagebox.askokcancel(title="Notification", message="Do you want to save?")
    # Check if fields are empty.
    if not site_text or not email_text or not pass_text:
        ok_to_save = False
        messagebox.showinfo(title="Error", message="Please don't leave any fields blank!")
    # We need to save the site, email, and pass into a text file.
    if ok_to_save:
        # with open(file="secret_data.json", mode="w") as secret_file:
        #     json.dump(json_data, secret_file, indent=4)
        # with open(file="secret_data.json", mode="r") as secret_file:
        #     secret_data = json.load(secret_file)
        #     # JSON data is actually a python dict.
        #     print(type(secret_data))
        #     print(secret_data)
        try:
            with open(file="secret_data.json", mode="r") as secret_file:
                # Read old data.
                secret_data = json.load(secret_file)
                # Update old data with new data (appending).
        except: # FileNotFoundError("File not found. Creating it now."):
            print("File not found. Creating it now.")
            with open(file="secret_data.json", mode="w") as secret_file:
                json.dump(json_data, secret_file, indent=4)
        else:
            secret_data.update(json_data)
            with open(file="secret_data.json", mode="w") as secret_file:
                # Save the new data
                json.dump(secret_data, secret_file, indent=4)
        finally:
            web_entry.delete(0, END)
            pass_entry.delete(0, END)
    
    
        # with open(file="secret_data.txt", mode="a") as secret_file:
            # secret_file.write(f"{site_text} | {email_text} | {pass_text}\n")
        # Clear the entries.

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)

web_label = Label(text="Website:", font=(FONT_NAME, 14))
web_label.grid(row=1, column=0)
user_label = Label(text="Email/Username:", font=(FONT_NAME, 14))
user_label.grid(row=2, column=0)
pass_label = Label(text="Password:", font=(FONT_NAME, 14))
pass_label.grid(row=3, column=0)

web_entry = Entry(width=21)
web_entry.grid(row=1, column=1)
# Start the cursor in this entry.
web_entry.focus()
user_entry = Entry(width=38)
user_entry.grid(row=2, column=1, columnspan=2)
# You can set whatever your most commonly used email is as the default value.
user_entry.insert(0, "sample_email@gmail.com")
pass_entry = Entry(width=21)
pass_entry.grid(row=3, column=1)

search_button = Button(text="Search", command=search_pass, width=13)
search_button.grid(row=1, column=2)
gen_button = Button(text="Generate Password", command=gen_pass)
gen_button.grid(row=3, column=2)
add_button = Button(text="Add", command=add_pass, width=36)
add_button.grid(row=4, column=1, columnspan=2)
window.mainloop()