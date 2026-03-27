import turtle
import pandas

# Turtle just works with image.gif

screen = turtle.Screen()
screen.title("U.S States Games")
image = "./Day_25_CSV_Files_Pandas/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("./Day_25_CSV_Files_Pandas/50_states.csv")

answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?").capitalize()

if answer_state in data["state"]:
    print("yes")







screen.exitonclick()