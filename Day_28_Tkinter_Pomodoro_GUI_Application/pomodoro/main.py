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
def start_timer():
    count_down(10)
    

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    canvas.itemconfig(timer_text, text= count)
    if count > 0:
        window.after(1000, count_down, count - 1)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx= 100, pady= 50, bg= YELLOW)


# Title Label -----------------------------------------------------------------------------------------------------------
label_timer = Label(text="Timer",fg= GREEN, bg= YELLOW, font=(FONT_NAME, 50))
label_timer.grid(row= 1, column= 2)


# Canvas -----------------------------------------------------------------------------------------------------------
canvas = Canvas(width= 200, height= 224, bg= YELLOW, highlightthickness= 0) # for put images in tkinter we should learn Canvas Widget
tomato_img = PhotoImage(file="./Day_28_Tkinter_Pomodoro_GUI_Application/pomodoro/tomato.png")
canvas.create_image(100, 112, image= tomato_img)
timer_text = canvas.create_text(100, 130, text= "00:00", fill="white",font= (FONT_NAME, 35, "bold"))
canvas.grid(row= 2, column= 2)



# Button(Start) -----------------------------------------------------------------------------------------------------------
button_start = Button(text= "Start", font= (FONT_NAME, 15, "bold"), bg= YELLOW, highlightthickness= 0)
button_start.grid(row= 3, column= 1)


# Button(Reset) -----------------------------------------------------------------------------------------------------------
button_reset = Button(text= "Reset", font= (FONT_NAME, 15, "bold"), bg= YELLOW, highlightthickness= 0)
button_reset.grid(row= 3, column= 3)


# Check mark Label -----------------------------------------------------------------------------------------------------------
check_marks = Label(text="✓", fg= GREEN, bg= YELLOW, font=(FONT_NAME, 35, "bold"))
check_marks.grid(row= 4, column= 2)


window.mainloop()