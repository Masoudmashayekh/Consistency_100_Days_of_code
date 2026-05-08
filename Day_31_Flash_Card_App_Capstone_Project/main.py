BACKGROUND_COLOR = "#B1DDC6"

                                            
#----------------------------------------------
import tkinter
from tkinter import Canvas, PhotoImage



window = tkinter.Tk()
window.title("Flashy")
window.config(padx= 50, pady= 50)


canves = Canvas(height= 200, width= 200)
front_img = PhotoImage(file= "Day_31_Flash_Card_App_Capstone_Project/images/card_front.png")
canves.create_image(800, 526, image = front_img)
canves.pack()





window.mainloop()