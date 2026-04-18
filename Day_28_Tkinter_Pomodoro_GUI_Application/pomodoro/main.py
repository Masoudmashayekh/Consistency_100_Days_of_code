from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx= 100, pady= 50)


canvas = Canvas(width= 200, height= 224) # for put images in tkinter we should learn Canvas Widget
tomato_img = PhotoImage(file="./Day_28_Tkinter_Pomodoro_GUI_Application/pomodoro/tomato.png")
canvas.create_image(103, 112, image= tomato_img)
canvas.create_text(103, 130, text= "00:00", fill="white",font= (FONT_NAME, 35, "bold"))
canvas.pack()








window.mainloop()