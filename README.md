[Read the document online](https://docs.google.com/document/d/e/2PACX-1vQDWwU2YIUfiRs8i48olrLBeGFRHYXomFZ6ZBVlp9WHMPDp0LefkQzgqPjsIhOxSEAXOupzDcU2vkDR/pub)

# 🐍 100 Days of Code: Python
Welcome to my journey through the **100 Days of Code** challenge! This repository serves as a digital log of my progress, daily learnings, and the projects I build along the way.

## 🗒️ Daily Log

### 📂 Day 1: Working with Variables to Manage Data

**Topic:** Python Basics & String Manipulation

Today, I focused on the absolute building blocks of Python. I learned how to interact with the console and how to handle basic data types.

#### 🗝️ Key Concepts
* **Printing:** Using `print()` to display text or instructions.
* **Strings:** 
    * Enclosed in `" "` or `' '`.
    * **Concatenation:** Combine strings using the `+` operator.
    * **Escape Characters:** Use `\n` for new lines.
* **Comments:** Start with `#` to explain what the code is doing.
* **Variables:** Store data for later use (e.g., `name = "Hello"`).
* **String Length:** Use `len()` to get the number of characters in a string.
* **User Input:** `input()` gets data from the user as a string.

#### 🛠️ Code Snippets
```python
# This is a comment - it's ignored by the computer!
name = input("What is your name? ")
print("Hello " + name + "!\nYour name has " + str(len(name)) + " characters.")
```



### 📂 Day 2: Understanding Data Types & Manipulating Numbers

**Topic:** Primitive Data Types, Type Conversion, and f-Strings

Today, I explored how Python handles different kinds of data under the hood and how to perform mathematical operations while keeping the output clean and readable.

#### 🗝️ Key Concepts

* **Data Types:** Python has 4 primary types:
    * **Strings (str):** Text inside `" "` or `' '`. Use indexing `[ ]` to get specific characters (e.g., `"Hello"[0]` → `H`).
    * **Integers (int):** Whole numbers. Use `_` for readability (e.g., `1_000_000`).
    * **Floats (float):** Numbers with decimals (e.g., `3.14`).
    * **Booleans (bool):** Only `True` or `False`.
* **Type Management:**
    * **Type Checking:** Use `type()` to identify the class of a variable (e.g., `type(123)` → `<class 'int'>`).
    * **Type Conversion:** Convert between types using `int()`, `str()`, or `float()`.
* **Math & Shorthand:**
    * **Rounding:** Use `round(number, decimals)` to control decimal places.
    * **Shorthand Operators:** Use `+=`, `-=`, `*=`, and `/=` to update variable values quickly.
* **f-Strings:** Insert variables into strings easily by placing an `f` before the quotes and using curly braces: `f"Your score is {score}"`.

#### 🛠️ Code Snippets
```python
# BMI Calculation Example
height = 1.65
weight = 84

# Calculation using exponent (**)
bmi = weight / (height ** 2)

# Output using f-String and Rounding
print(f"Height: {height}m, Weight: {weight}kg")
print(f"Your calculated BMI is: {round(bmi, 2)}")

# Shorthand usage
score = 0
score += 1 # score is now 1
```



### 📂 Day 3: Conditional Statements & Logical Operators

**Topic:** Control Flow and Decision Making

Today, I taught the computer how to make decisions based on specific conditions. I learned how to guide the program through different execution paths using logic and user input.

#### 🗝️ Key Concepts

* **Conditional Statements:**
    * **`if` / `elif` / `else`:** Python evaluates conditions from top to bottom.
    * **Nested Conditions:** An `if` statement inside another `if` for multi-step logic.
    * **Multiple `if` Statements:** Used when multiple conditions can be true simultaneously (unlike `elif`, which stops after the first true condition).
* **Comparison Operators:**
    * `>` (Greater than), `<` (Less than), `>=` (Greater or equal), `<=` (Less or equal).
    * `==` (Equal to), `!=` (Not equal).
    * **Note:** `=` assigns a value; `==` checks for equality.
* **Modulo Operator (%):** Returns the remainder of a division. 
    * `10 % 2 == 0` (Even)
    * `10 % 3 == 1` (Odd)
* **Logical Operators:**
    * `and`: Both conditions must be True.
    * `or`: At least one condition must be True.
    * `not`: Reverses the boolean value (True becomes False).
* **Input Handling:**
    * `.upper()`: Converts input to uppercase (e.g., "y" → "Y").
    * `.capitalize()`: Capitalizes the first letter (e.g., "left" → "Left").

#### 🛠️ Code Snippets
```python
# Rollercoaster Ticket Logic
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
    elif age <= 18:
        bill = 7
    else:
        bill = 12
    
    wants_photo = input("Do you want a photo taken? Y or N: ").upper()
    if wants_photo == "Y":
        bill += 3
        
    print(f"Your final bill is ${bill}")
else:
    print("Sorry, you have to grow taller before you can ride.")
```



### 📂 Day 4: Randomization & Python Lists

**Topic:** Generating Randomness and Organizing Data in Lists

Today, I explored how to introduce uncertainty into programs using the `random` module and how to store related data using lists and nested structures.

#### 🗝️ Key Concepts

* **Randomization (The `random` Module):**
    * `random.randint(a, b)`: Returns a random integer between $a$ and $b$ (inclusive).
    * `random.random()`: Returns a random float between 0.0 and 1.0 (excluding 1.0).
    * `random.uniform(a, b)`: Returns a random float between $a$ and $b$.
    * `random.choice(list)`: Picks a random item from a list.
* **Modules:**
    * Used to break down large programs into smaller, manageable files.
    * You can import built-in modules or custom ones using `import my_module`.
* **Lists & Nested Lists:**
    * **Regular List:** An ordered collection of items (e.g., `fruits = ["Apple", "Banana"]`).
    * **Adding Items:** Use `.append("new_item")` to add data to the end of a list.
    * **Nested Lists:** A list containing other lists (e.g., `dirty_dozen = [fruits, vegetables]`).
    * **Accessing Data:** Use indices (e.g., `list[0]`). For nested lists, use double indices (e.g., `dirty_dozen[0][1]` to get the second item of the first list).

#### 🛠️ Code Snippets
```python
import random

# Mini Rock Paper Scissors
choices = ["Rock", "Paper", "Scissors"]
pc_choice = random.choice(choices)
user_index = int(input("0=Rock, 1=Paper, 2=Scissors: "))
my_choice = choices[user_index]

print(f"Computer chose {pc_choice}")

if my_choice == pc_choice:
    print("Draw")
elif (my_choice == "Rock" and pc_choice == "Scissors") or \
     (my_choice == "Paper" and pc_choice == "Rock") or \
     (my_choice == "Scissors" and pc_choice == "Paper"):
    print("You win!")
else:
    print("You lose!")
```



### 📂 Day 5: Loops, Range, and the Password Generator

**Topic:** For Loops, Range, and List Shuffling

Today, I learned how to automate repetitive tasks using loops. I explored how to iterate through lists, work with numerical ranges, and build a secure password generator by shuffling character sets.

#### 🗝️ Key Concepts

* **For Loops:** Used to iterate over a list, string, or any sequence.
    * **Syntax:** `for item in list:`
    * Useful for calculating totals or finding the highest value in a dataset.
* **The `range()` Function:** Generates a sequence of numbers.
    * `range(1, 10)` → Numbers 1 to 9 (stops before 10).
    * `range(1, 10, 3)` → Numbers 1, 4, 7 (increments by 3).
* **Built-in Functions for Lists:**
    * `sum(list)`: Quickly totals all numbers in a list.
    * `max(list)` / `min(list)`: Returns the highest or lowest value.
* **Randomization & Strings:**
    * `random.shuffle(list)`: Rearranges the order of items in a list in-place.
    * `''.join(list)`: Concatenates all items in a list into a single string.

#### 🛠️ Code Snippets
```python
# FizzBuzz Challenge
for n in range(1, 101):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)

# Password Generator Logic (Hard Version)
import random
password_list = ["a", "b", "c", "1", "2", "3", "!", "#"]
random.shuffle(password_list) # Shuffles the list order
password = "".join(password_list) # Converts list back to string
print(f"Your secure password is: {password}")
```



### 📂 Day 6: Functions & While Loops

**Topic:** Defining Functions and Controlling Logic with While Loops

Today, I focused on code reusability by defining my own functions and learned how to use `while` loops to repeat actions as long as a specific condition remains true. I applied these concepts to solve navigation puzzles in Reeborg's World.

#### 🗝️ Key Concepts

* **Functions:** Used to wrap a block of code so it can be executed multiple times without rewriting it.
    * **Defining:** `def my_function():`
    * **Calling:** `my_function()`
    * **Indentation:** Python uses 4 spaces (or one Tab) to determine what code belongs inside the function.
* **While Loops:** Repeats code while a condition is `True`. 
    * Unlike `for` loops (which iterate over a set number of items), `while` loops are used when you don't know how many times the loop needs to run beforehand.
    * ⚠️ **Warning:** If the condition never becomes `False`, you create an "infinite loop," which can crash the program.
* **Reeborg's World Logic:**
    * **Custom Maneuvers:** Creating `turn_right()` by calling `turn_left()` three times.
    * **Conditional Navigation:** Combining `while` loops with `if/elif/else` statements to check if the front is clear or if a wall is in the way.
    * **The Right-Hand Rule:** An algorithm used to solve mazes by always prioritizing turning right whenever possible.

#### 🛠️ Code Snippets
```python
# Function Definition
def greet_user():
    print("Hello!")
    print("Welcome to Day 6.")

greet_user()

# While Loop Example
count = 5
while count > 0:
    print(f"Counting down: {count}")
    count -= 1
print("Blast off!")

# Reeborg Navigation Pattern (Right-Hand Rule)
def navigate_maze():
    while not at_goal():
        if right_is_clear():
            turn_right()
            move()
        elif front_is_clear():
            move()
        else:
            turn_left()
```




### 📂 Day 7: Hangman Project

**Topic:** Logic Integration and Game Development

Today was a capstone-style project where I combined loops, conditionals, and list manipulation to build a complete Hangman game. I learned how to manage complex game states and use external modules to keep code organized.

#### 🗝️ Key Concepts

* **External Modules:** Importing word lists and ASCII art from separate files (`hangman_words.py`, `hangman_art.py`) to keep the main script clean.
* **Game Setup:**
    * **Random Selection:** Using `random.choice()` to pick the secret word.
    * **Placeholders:** Creating a list of underscores `["_"]` to represent the hidden letters and tracking the player's progress.
    * **Life Management:** Initializing a `lives` variable (set to 6) to track failed attempts.
* **The Game Loop:**
    * **Continuous Play:** Using `while not game_over` to keep the game running.
    * **String Join:** Using `" ".join(list_name)` to display the current state of the word (e.g., `a _ _ l e`) to the user.
* **Conditional Logic:**
    * Checking if the guessed letter has been guessed before.
    * Updating the placeholder list if the guess is correct.
    * Decrementing `lives` and displaying the corresponding ASCII hangman stage if the guess is wrong.
* **Win/Loss Conditions:** Logic to detect when no more underscores remain (Win) or when lives reach zero (Loss).

#### 🛠️ Code Snippets
```python
import random
from hangman_art import HANGMANPICS

chosen_word = "apple"
display = ["_", "_", "_", "_", "_"]
lives = 6
game_over = False

while not game_over:
    guess = input("Guess a letter: ").lower()
    
    # Check if letter is in word
    if guess in chosen_word:
        for position in range(len(chosen_word)):
            if chosen_word[position] == guess:
                display[position] = guess
    else:
        lives -= 1
        print(HANGMANPICS[6 - lives])

    print(f"{' '.join(display)}")

    if "_" not in display:
        game_over = True
        print("You win!")
    elif lives == 0:
        game_over = True
        print(f"You lose! The word was {chosen_word}.")
```



### 📂 Day 8: Functions with Inputs & Caesar Cipher

**Topic:** Function Parameters, Keyword Arguments, and Cipher Logic

Today, I moved beyond simple functions to explore how to pass data into them. I learned the difference between positional and keyword arguments and applied these skills to build a functional Caesar Cipher encryption tool.

#### 🗝️ Key Concepts

* **Parameters vs. Arguments:**
    * **Parameter:** The name of the data being passed in (the "placeholder" defined in the function).
    * **Argument:** The actual value or data sent to the function when it is called.
* **Positional vs. Keyword Arguments:**
    * **Positional:** Arguments assigned based on the order they are passed.
    * **Keyword:** Arguments assigned by name (e.g., `greet(name="Alice", location="London")`), making the code more readable and order-independent.
* **Modular Arithmetic in Logic:** Using the modulo operator (`%`) to ensure that when shifting letters at the end of the alphabet (like 'z'), the index wraps back around to the beginning.
* **Input Normalization:** Using `.lower()` to ensure user input matches the expected format for comparison logic.

#### 🛠️ Code Snippets
```python
# Function with Multiple Keyword Arguments
def greet_with(name, location):
    print(f"Hello {name}!")
    print(f"What is it like in {location}?")

# Calling with keyword arguments
greet_with(location="London", name="Masoud")

# Core Caesar Cipher Logic
def caeser(text, shift, direction):
    if direction == "decode":
        shift *= -1
    
    # alphabet logic using modulo for wrapping
    # "".join(alphabet[(alphabet.index(char) + shift) % 26] ...)
```