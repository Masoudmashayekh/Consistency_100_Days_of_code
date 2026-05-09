BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Courier"
                                            
#----------------------------------------------
from tkinter import *



window = Tk()
window.title("Flashy")
window.minsize(height= 750, width=950)
window.config(padx= 50, pady= 50, bg= BACKGROUND_COLOR)

# Front --------------------------------------------------------
canves = Canvas(height=526, width= 800)
canves.config(bg= BACKGROUND_COLOR, highlightthickness= 0)
front_img = PhotoImage(file= "Day_31_Flash_Card_App_Capstone_Project/images/card_front.png")
canves.create_image(400, 270, image = front_img)
canves.create_text(400, 100, text=f"English", font=(FONT_NAME, 30))
canves.create_text(400, 270, text="Word", font=(FONT_NAME, 50, "bold"))
canves.grid(row= 1, column= 1, columnspan= 2)


# Button Right --------------------------------------------------------
image_right = PhotoImage(file= "Day_31_Flash_Card_App_Capstone_Project/images/right.png")
button_right = Button(image= image_right,padx= 50 ,bg= BACKGROUND_COLOR, highlightthickness= 0)
button_right.grid(row= 2, column= 2)

# Button Wrong --------------------------------------------------------
image_wrong = PhotoImage(file= "Day_31_Flash_Card_App_Capstone_Project/images/wrong.png")
button_wrong = Button(image= image_wrong, highlightthickness= 0)
button_wrong.grid(row= 2, column= 1)




window.mainloop()