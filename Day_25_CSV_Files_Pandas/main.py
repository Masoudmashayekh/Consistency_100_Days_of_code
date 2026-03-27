import turtle
import pandas
# Turtle just works with image.gif
data = pandas.read_csv("./Day_25_CSV_Files_Pandas/50_states.csv")
# df = data.data
# print(df)



screen = turtle.Screen()
screen.title("U.S States Games")
image = "./Day_25_CSV_Files_Pandas/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")

x = data[data.state == "Alabama"]
x_x = x.y
print(x_x)





screen.exitonclick()