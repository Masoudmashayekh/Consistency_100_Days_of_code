import tkinter

window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width= 300, height= 150)

# label_equal ---------------------------------------
label_equal = tkinter.Label(text= "is equal to: ", font=("Arial", 14, "bold"))
label_equal.grid(row= 2, column= 1)
label_equal.config(padx= 10, pady= 10)

# label_miles_number ---------------------------------------
label_miles_number = tkinter.Label(text= "0", font= ("Arial", 14, "bold"))
label_miles_number.grid(row= 1, column= 2)
label_miles_number.config(padx= 10, pady= 10)

# label_km_number ---------------------------------------
label_km_number = tkinter.Label(text= "0", font= ("Arial", 14, "bold"))
label_km_number.grid(row= 2, column= 2)
label_km_number.config(padx= 10, pady= 10)

# label_miles ---------------------------------------
label_miles = tkinter.Label(text= "Miles", font= ("Arial", 14, "bold"))
label_miles.grid(row= 1, column= 3)
label_miles.config(padx= 10, pady= 10)

# label_km ---------------------------------------
label_km = tkinter.Label(text= "Km", font= ("Arial", 14, "bold"))
label_km.grid(row= 2, column= 3)
label_km.config(padx= 10, pady= 10)

# Button ---------------------------------------
calculate_button = tkinter.Button(text= "Calculte")
calculate_button.grid(row= 3, column= 2)






window.mainloop()