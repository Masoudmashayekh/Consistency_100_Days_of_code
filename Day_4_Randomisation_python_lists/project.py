import random
list= ["Rock", "Paper", "Scissors"]
pc_choice = random.choice(list)
my_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
print(f"Pc chose: {pc_choice}")
print(f"My chose: {list[my_choice]}")
if list[my_choice] == pc_choice:
    print("It's a draw.")
elif list[my_choice] == list[0] and pc_choice == list[2]:
    print("You win!")
elif list[my_choice] == list[1] and pc_choice == list[0]:
    print("You win!")
elif list[my_choice] == list[2] and pc_choice == list[1]:
    print("You win!")
elif list[my_choice] == list[0] and pc_choice == list[1]:
    print("You Lose!")
elif list[my_choice] == list[1] and pc_choice == list[2]:
    print("You Lose!")
elif list[my_choice] == list[2] and pc_choice == list[0]:
    print("You Lose!")