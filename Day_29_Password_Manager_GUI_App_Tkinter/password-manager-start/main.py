from tkinter import *
FONT = ("Arial", 14, "bold")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.minsize(width= 200, height= 200)
window.config(padx= 20, pady= 20)

canvas = Canvas(width= 200, height= 200, highlightthickness=0)
logo_img = PhotoImage(file="./Day_29_Password_Manager_GUI_App_Tkinter/password-manager-start/logo.png")
canvas.create_image(100, 100, image= logo_img)
canvas.pack()

# Label: Website
label_website = Label(text= "Website:", font= FONT)
label_website.pack()
# Input: Website
input_website = Entry(width= 35)
input_website.pack()


# Label: Email / Username
label_username = Label(text= "Email/username:")
label_username.pack()
# Input: Email / Username
input_username = Entry(width= 35)
input_username.pack()

# Label: Password
label_password = Label(text= "Password:")
label_password.pack()
# Input: Password
input_password = Entry(width= 21)

# Button: Generate Password
button_password = Button(text= "Generate Password", command= "")









window.mainloop()

