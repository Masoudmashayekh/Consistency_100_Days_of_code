BACKGROUND_COLOR = "#B1DDC6"

                                            
#----------------------------------------------
import tkinter
from tkinter import Canvas, PhotoImage



window = tkinter.Tk()
window.title("Flashy")
window.minsize(height= 750, width=950)
window.config(padx= 50, pady= 50)

# Front --------------------------------------------------------
canves = Canvas(height=526, width= 800)
front_img = PhotoImage(file= "Day_31_Flash_Card_App_Capstone_Project/images/card_front.png")
canves.create_image(400, 270, image = front_img)
canves.pack()





window.mainloop()