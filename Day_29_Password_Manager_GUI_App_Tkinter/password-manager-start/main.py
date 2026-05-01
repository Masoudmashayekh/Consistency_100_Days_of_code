from tkinter import *
from tkinter import messagebox



FONT = ("Arial", 14, "bold")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    website = input_website.get()
    username = input_username.get()
    password = input_password.get()
    
    messagebox.askokcancel(title= website, message= f"These are the details entered: \nEmail: {username} \nPassword: {password} \nIs it ok to save?")
    
    with open("Day_29_Password_Manager_GUI_App_Tkinter/password-manager-start/data.txt", "a") as file:
        file.write(f"{website} | {username} | {password} \n")
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
button_password = Button(text= "Generate Password", command= "")
button_password.grid(row= 4, column= 3)
# Button: Add -----------------------------------
button_add = Button(text= "Add", width= 36, command= save_password)
button_add.grid(row= 5, column= 2, columnspan= 2)









window.mainloop()

