import random
list= ["Rock", "Paper", "Scissors"]
pc_chose = random.choice(list)
my_chose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
print(f"Pc chose: {pc_chose}")
print(f"My chose: {list[my_chose]}")
if list[my_chose] == pc_chose:
    print("It's a draw.")
elif list[my_chose] == list[0] and pc_chose == list[2]:
    print("You win!")
elif list[my_chose] == list[1] and pc_chose == list[0]:
    print("You win!")
elif list[my_chose] == list[2] and pc_chose == list[1]:
    print("You win!")
elif list[my_chose] == list[0] and pc_chose == list[1]:
    print("You Lose!")
elif list[my_chose] == list[1] and pc_chose == list[2]:
    print("You Lose!")
elif list[my_chose] == list[2] and pc_chose == list[0]:
    print("You Lose!")