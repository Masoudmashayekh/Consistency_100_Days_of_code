# Debugging
# Grace Hopper
# Everyone gets bugs.
# 1. Describe the problem

def my_function():
    for i in range(1, 20): # 21 not 20
        if i == 20:
            print("You got it.")
            
my_function()

# Describe the Problem - Write your answers as comments:
# What is the for loop doing?
# When is the function meant to print "You got it"?
# What are your assumptions about the value of i ? 1, 2, 3, 4, . . . , 19


# 2. Reproduce the Bug
from random import randint
dice_images = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]
dice_num = randint(6, 8)
print(dice_images[dice_num])
