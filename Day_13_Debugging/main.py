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
    
    
# 5. Print is your friend. BFF

word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page == int(input("Number of words per pages: ")) # = insted of ==
total_words = pages * word_per_page
print(total_words)


# 6. Use a Debugger
import random
import maths

def mutate(a_list):
    b_list = []
    new_item = 0 
    for item in a_list:
        new_item = item * 2
        new_item += random.randint(1, 3)
        new_item = maths.add(new_item, item)
        b_list.append(new_item)
    print(b_list)
    
mutate([1, 2, 3, 5, 8, 12])



# 7. Take a Break
# It's really, really important when you're just staring at the code and you keep looking at it, it's not going to tell you the solution. Just have a cup of tea or have a nap, or just go to sleep and try to tackle it tomorrow.

# 8. Ask a Friend
# The really good thing about asking a friend to look through your code is they won't make the same assumptions that you've made. So they have some fresh eyes that they can look at the code with, and it might be incredibly obvious what's actually happening. And it's really not embarrassing at all.

# 9. Run Often
# what I mean is run your code often. Don't wait until you've written loads and loads of code to hit run and then find out you've got loads of snags and loads of bugs. But run it after every little execution.