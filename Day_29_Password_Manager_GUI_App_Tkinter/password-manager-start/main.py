from tkinter import *
FONT = ("Arial", 14, "bold")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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


# Label: Email / Username --------------------------
label_username = Label(text= "Email/username:", font= FONT)
label_username.grid(row= 3, column= 1)
# Input: Email / Username -------------------------
input_username = Entry(width= 38)
input_username.grid(row= 3, column= 2, columnspan= 2)

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
button_add = Button(text= "Add", width= 36, command= "")
button_add.grid(row= 5, column= 2, columnspan= 2)









window.mainloop()

