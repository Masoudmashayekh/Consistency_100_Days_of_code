import random
list= ["Rock", "Paper", "Scissors"]
list_len = len(list)
pc_score = 0
my_score = 0
pc_chose = random.choice(list)
my_chose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

if my_chose == list[0] and pc_chose == list[0]:
    print("It's a draw.")
elif my_chose == list[0] and pc_chose == list[2]:
    print("You win!")
elif my_chose == list[2] and pc_chose == list[1]:
    print("You win!")
elif my_chose == list[0] and pc_chose == list[1]:
    print("You Lose!")
elif my_chose == list[1] and pc_chose == list[2]:
    print("You Lose!")