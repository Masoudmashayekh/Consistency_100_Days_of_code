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

guess_list = []
while len(guess_list) < 50:
    answer_state = screen.textinput(title= f"{len(guess_list)}/50 states correct", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guess_list:
                missing_states.append(state)
        print(missing_states)
        break

    if answer_state in all_states:
        guess_list.append(answer_state)
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(state_data.state.item())






# screen.exitonclick()