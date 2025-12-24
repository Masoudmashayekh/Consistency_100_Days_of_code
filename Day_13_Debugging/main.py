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
dice_num = randint(0, 5) # range should be (0, 5) not (1, 6)
print(dice_images[dice_num])


# 3. Play Computer
year = int(input("What's your year of birth? "))

if year > 1980 and year <= 1994:  # should use year <= 1994 instead of year < 1994
    print("You are a millennial.")
elif year > 1994:
    print("You are a Gen Z.")
    
    
# 4. Fix the Errors
try:
    age = int(input("How old are you?"))
except ValueError:
    print("You have typed in an invalid number. Please try again.")
    age = int(input("How old are you?"))  
    
    
if age > 18:
    print(f"You can drive at age {age}")