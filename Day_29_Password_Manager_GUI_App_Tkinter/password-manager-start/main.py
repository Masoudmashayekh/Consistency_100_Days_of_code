from tkinter import *



# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.minsize(width= 500, height= 500)

canvas = Canvas(width= 200, height= 200, highlightthickness=0)
luck_img = PhotoImage(file="./Day_29_Password_Manager_GUI_App_Tkinter/password-manager-start/logo.png")
canvas.create_image(100, 100, image= luck_img)
canvas.pack()







window.mainloop()

