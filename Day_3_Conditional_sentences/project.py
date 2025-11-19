print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
left_right = input("left or right? ").capitalize()
swim_wiat = input("swim or wait? ").capitalize()
which_door = input("Which door? Red, Blue, Yellow: ").capitalize()
if left_right == "Right":
    print("Game Over.")
else:
    if swim_wiat == "Swim":
        print("Game Over.")
    else:
        if which_door == "Red" or which_door == "Blue":
            print("Game Over.")
        elif which_door == "Yellow":
            print("You Win!")