import turtle
# Turtle just works with image.gif

screen = turtle.Screen()
screen.title("U.S States Games")
image = "./Day_25_CSV_Files_Pandas/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")







screen.exitonclick()