print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
left_right = input("left or right? ").capitalize()
if left_right == "Right":
    print("Game Over.")
    quit
else:
    swim_wiat = input("swim or wait? ").capitalize()
    if swim_wiat == "Swim":
        print("Game Over.")
        quit
    else:
        which_door = input("Which door? Red, Blue, Yellow: ").capitalize()
        if which_door == "Red" or which_door == "Blue":
            print("Game Over.")
            quit
        elif which_door == "Yellow":
            print("You Win!")
