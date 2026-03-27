import turtle
import pandas

# Turtle just works with image.gif

screen = turtle.Screen()
screen.title("U.S States Games")
image = "./Day_25_CSV_Files_Pandas/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("./Day_25_CSV_Files_Pandas/50_states.csv")
all_states = data["state"].to_list()


answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?").capitalize()


if answer_state in all_states:
    t = turtle.Turtle()
    t.penup()
    t.hideturtle()
    state_data = data[data.state == answer_state]
    t.goto(int(state_data.x), int(state_data.y))
    t.write(answer_state)






screen.exitonclick()