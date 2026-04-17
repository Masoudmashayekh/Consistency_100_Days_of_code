import tkinter

window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width= 300, height= 300)

# Label ---------------------------------------
label_equal = tkinter.Label(text= "is equal to: ", font=("Arial", 14, "bold"))
label_equal.grid(row= 2, column= 1)
label_equal.config(padx= 20, pady= 20)

# Label ---------------------------------------
label_mlies_number = tkinter.Label(text= "0", font= ("Arial", 14, "bold"))
label_mlies_number.grid(row= 1, column= 2)

# Label ---------------------------------------

# Label ---------------------------------------

# Label ---------------------------------------






window.mainloop()