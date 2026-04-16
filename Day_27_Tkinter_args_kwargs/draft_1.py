# Day 27: Tkinter, *args, **kwargs and creating GUI programs
# GUI : Graphical User Interface
# tkinter documentation: https://www.tcl-lang.org/man/tcl8.6/TkCmd/entry.htm

import tkinter
# from tkinter import *

def button_clicked():
    new_text = input.get()
    my_label.config(text= new_text)


window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label:------------------------------------------------------------------------------
my_label = tkinter.Label(text="I am a Label",font=("Arial", 14, "bold"))
# my_label["text"] = "New Text 1"
# or
my_label.config(text="New Text 2")

# my_label.pack() # this line is important for showing my_label
my_label.grid(row= 1, column= 1)

# Button:------------------------------------------------------------------------------
button = tkinter.Button(text = "Click me!", command = button_clicked) # no need () in button_clicked function in command.
# button.pack()
button.grid(row= 2, column= 2)

# Entry:------------------------------------------------------------------------------
input = tkinter.Entry(width= 10)
# input.pack()
input.grid(row=3, column= 4)

# New button:------------------------------------------------------------------------------
new_button = tkinter.Button(text="New button")
new_button.grid(row= 1, column= 3)

# Pack() , Place(x, y) , Grid

window.mainloop()
    

