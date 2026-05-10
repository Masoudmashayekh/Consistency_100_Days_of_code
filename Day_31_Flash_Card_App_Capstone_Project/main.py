BACKGROUND_COLOR = "#B1DDC6"
# FONT_NAME = "Courier"
FONT_NAME = "Ariel"
                                            
#----------------------------------------------
from tkinter import *
import pandas
import random
import time

# Data -------------------------------------------
data= pandas.read_csv("./Day_31_Flash_Card_App_Capstone_Project/data/words_to_learn.csv")
to_learn = data.to_dict(orient= "records")
current_card = {}

def call_next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canves.itemconfig(card_title, text= "Italian", fill= "black")
    canves.itemconfig(card_word, text= f"{current_card["italian"]}", fill= "black")
    canves.itemconfig(card_background, image= card_front_img)
    flip_timer = window.after(3000, func= flip_card)

def flip_card():
    canves.itemconfig(card_background, image= card_back_img)
    canves.itemconfig(card_title, text= "English", fill= "white")
    canves.itemconfig(card_word, text= f"{current_card["english"]}", fill= "white")
    
def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("./Day_31_Flash_Card_App_Capstone_Project/data/words_to_learn.csv")
    
    call_next_card()
    
    
    


# Tk --------------------------------------------------------
window = Tk()
window.title("Flashy")
# window.minsize(height= 750, width=950)
window.config(padx= 50, pady= 50, bg= BACKGROUND_COLOR)

flip_timer = window.after(3000, func= flip_card)

# Front card --------------------------------------------------------
canves = Canvas(height=526, width= 800, bg= BACKGROUND_COLOR, highlightthickness= 0)
card_front_img = PhotoImage(file= "Day_31_Flash_Card_App_Capstone_Project/images/card_front.png")
card_back_img = PhotoImage(file= "Day_31_Flash_Card_App_Capstone_Project/images/card_back.png")
card_background = canves.create_image(400, 263, image = card_front_img)
card_title = canves.create_text(400, 130, text=f"Title", font=(FONT_NAME, 40, "italic"))
card_word = canves.create_text(400, 263, text="Word", font=(FONT_NAME, 60, "bold"))
canves.grid(row= 1, column= 1, columnspan= 2)


# Button Right --------------------------------------------------------
right_img = PhotoImage(file= "Day_31_Flash_Card_App_Capstone_Project/images/right.png")
unknown_button = Button(image= right_img,padx= 50 ,bg= BACKGROUND_COLOR, highlightthickness= 0, command= is_known)
unknown_button.grid(row= 2, column= 2)

# Button Wrong --------------------------------------------------------
wrong_img = PhotoImage(file= "Day_31_Flash_Card_App_Capstone_Project/images/wrong.png")
known_button = Button(image= wrong_img, highlightthickness= 0, command= call_next_card)
known_button.grid(row= 2, column= 1)





call_next_card()


print()  


window.mainloop()