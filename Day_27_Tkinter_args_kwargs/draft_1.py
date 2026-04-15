# Day 27: Tkinter, *args, **kwargs and creating GUI programs
# GUI : Graphical User Interface
# tkinter documentation: https://www.tcl-lang.org/man/tcl8.6/TkCmd/entry.htm

import tkinter
# from tkinter import *

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
#------------------------------------------------------------------------------
# Label:
my_label = tkinter.Label(text="I am a Label",font=("Arial", 14, "bold"))
my_label.pack() # this line is important for showing my_label

my_label["text"] = "New Text 1"
# or
my_label.config(text="New Text 2")
#------------------------------------------------------------------------------
# Button:
def button_clicked():
    my_label.config(text="Button Got Clicked.")

def show_input():
    my_label.config(text=f"{input.get()}")

button = tkinter.Button(text = "Click me!", command = show_input) # no need () in button_clicked function in command.
button.pack()
#------------------------------------------------------------------------------
# Entry:
input = tkinter.Entry(width= 10)
input.pack()





window.mainloop()
    

