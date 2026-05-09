BACKGROUND_COLOR = "#B1DDC6"
# FONT_NAME = "Courier"
FONT_NAME = "Ariel"
                                            
#----------------------------------------------
from tkinter import *



window = Tk()
window.title("Flashy")
# window.minsize(height= 750, width=950)
window.config(padx= 50, pady= 50, bg= BACKGROUND_COLOR)

# Front card --------------------------------------------------------
canves = Canvas(height=526, width= 800, bg= BACKGROUND_COLOR, highlightthickness= 0)
card_front_img = PhotoImage(file= "Day_31_Flash_Card_App_Capstone_Project/images/card_front.png")
canves.create_image(400, 263, image = card_front_img)
title = canves.create_text(400, 150, text=f"Title", font=(FONT_NAME, 40, "italic"))
word = canves.create_text(400, 263, text="Word", font=(FONT_NAME, 60, "bold"))
canves.grid(row= 1, column= 1, columnspan= 2)


# Button Right --------------------------------------------------------
right_img = PhotoImage(file= "Day_31_Flash_Card_App_Capstone_Project/images/right.png")
unknown_button = Button(image= right_img,padx= 50 ,bg= BACKGROUND_COLOR, highlightthickness= 0)
unknown_button.grid(row= 2, column= 2)

# Button Wrong --------------------------------------------------------
wrong_img = PhotoImage(file= "Day_31_Flash_Card_App_Capstone_Project/images/wrong.png")
known_button = Button(image= wrong_img, highlightthickness= 0)
known_button.grid(row= 2, column= 1)




window.mainloop()