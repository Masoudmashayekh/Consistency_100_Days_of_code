# Day 27: Tkinter, *args, **kwargs and creating GUI programs
# GUI : Graphical User Interface

import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label:
my_label = tkinter.Label(text="I am a Label",font=("Arial", 14, "bold"))
my_label.pack(side="left") # this line is important for showing my_label








window.mainloop()
    

