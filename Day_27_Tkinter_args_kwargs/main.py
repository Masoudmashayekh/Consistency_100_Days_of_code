import tkinter

window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width= 300, height= 300)

# Label ---------------------------------------
label_equal = tkinter.Label(text= "is equal to: ", font=("Arial", 14, "bold"))
label_equal.grid(row= 2, column= 1)
label_equal.config(padx= 10, pady= 10)

# Label ---------------------------------------
label_miles_number = tkinter.Label(text= "0", font= ("Arial", 14, "bold"))
label_miles_number.grid(row= 1, column= 2)
label_miles_number.config(padx= 10, pady= 10)

# Label ---------------------------------------

# Label ---------------------------------------

# Label ---------------------------------------






window.mainloop()