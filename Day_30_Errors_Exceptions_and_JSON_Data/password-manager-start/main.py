from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

FONT = ("Arial", 14, "bold")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def generate_password():
    
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    [password_list.append(random.choice(letters)) for char in range(nr_letters)]

    [password_list.append(random.choice(symbols)) for char in range(nr_symbols)]

    [password_list.append(random.choice(numbers)) for char in range(nr_numbers)]


    random.shuffle(password_list)

    password = "".join(password_list)
    input_password.delete(first= 0, last= END)
    input_password.insert(END, password)
    pyperclip.copy(password)
    
    # print(f"Your password is: {password}")

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    website = input_website.get()
    username = input_username.get()
    password = input_password.get()
    new_data = {
        website:{
            "email": username,
            "password": password,
        }
    }
    
    
    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showerror(title= "Oops", message= "Please don't leave any fields empty!")
    else:    
        is_ok = messagebox.askokcancel(title= website, message= f"These are the details entered: \nEmail: {username} \nPassword: {password} \nIs it ok to save?")
        
        if is_ok:
            try:
                with open("Day_30_Errors_Exceptions_and_JSON_Data/password-manager-start/data.json", "r") as file:
                    # Reading old data
                    data = json.load(file)
            except FileNotFoundError:
                with open("Day_30_Errors_Exceptions_and_JSON_Data/password-manager-start/data.json", "w") as file
                    # Saving updated data
                json.dump(new_data, file, indent= 4)
            else:
                # Updating old data with new data
                data.update(new_data)
                
            with open("Day_30_Errors_Exceptions_and_JSON_Data/password-manager-start/data.json", "w") as file:
                # Saving updated data
                json.dump(data, file, indent= 4)
            
            input_website.delete(first= 0, last= END)
            input_password.delete(first= 0, last= END)
            
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.minsize(width= 200, height= 200)
window.config(padx= 50, pady= 50)

canvas = Canvas(width= 200, height= 200, highlightthickness=0)
logo_img = PhotoImage(file="./Day_29_Password_Manager_GUI_App_Tkinter/password-manager-start/logo.png")
canvas.create_image(100, 100, image= logo_img)
canvas.grid(row= 1, column= 2)

# Label: Website ----------------------------------
label_website = Label(text= "Website:", font= FONT)
label_website.grid(row= 2, column= 1)
# Input: Website ----------------------------------
input_website = Entry(width= 38)
input_website.grid(row= 2, column= 2, columnspan= 2)
input_website.focus() # for cursor
print(type(input_website))

# Label: Email / Username --------------------------
label_username = Label(text= "Email/username:", font= FONT)
label_username.grid(row= 3, column= 1)
# Input: Email / Username -------------------------
input_username = Entry(width= 38)
input_username.grid(row= 3, column= 2, columnspan= 2)
input_username.insert(END, "masoud@yahoo.com")

# Label: Password --------------------------------
label_password = Label(text= "Password:", font= FONT)
label_password.grid(row= 4, column= 1)
# Input: Password --------------------------------
input_password = Entry(width= 21)
input_password.grid(row= 4, column= 2)

# Button: Generate Password ----------------------
button_password = Button(text= "Generate Password", command= generate_password)
button_password.grid(row= 4, column= 3)
# Button: Add -----------------------------------
button_add = Button(text= "Add", width= 36, command= save_password)
button_add.grid(row= 5, column= 2, columnspan= 2)









window.mainloop()

