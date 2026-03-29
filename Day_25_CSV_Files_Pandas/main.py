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

game_is_on = True
while game_is_on:
    answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?").capitalize()


    if answer_state in all_states:
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(state_data.state.item())






screen.exitonclick()