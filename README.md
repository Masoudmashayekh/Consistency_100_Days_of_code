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



### 📂 Day 9: Dictionaries & Nesting

**Topic:** Key-Value Pairs and Complex Data Structures

Today, I moved beyond lists to explore dictionaries, which allow for more structured data storage. I also learned how to nest lists and dictionaries inside one another to manage complex datasets.

#### 🗝️ Key Concepts

* **Basic Dictionaries:** Collections of data stored as `key : value` pairs.
    * **Access:** `dictionary["key"]`
    * **Add/Update:** `dictionary["new_key"] = value`
    * **Wipe:** `empty_dict = {}`
* **Looping:** When looping through a dictionary, the default behavior is to iterate over the **keys**. To get the values, use the key as an index: `dictionary[key]`.
* **Nesting:**
    * **List in a Dictionary:** Useful for associating multiple related items with a single key (e.g., `"France": ["Paris", "Lille"]`).
    * **Dictionary in a Dictionary:** Useful for storing detailed metadata (e.g., `"France": {"visits": 8, "cities": ["Paris", "Lille"]}`).
* **Finding the Max:** Using the `max()` function with a dictionary to identify the winner of the Secret Auction based on the highest value.

#### 🛠️ Code Snippets
```python
# Nested Dictionary Example
travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    },
}

# Finding the highest bidder in a dictionary
bids = {"Tom": 120, "Jerry": 150, "Spike": 100}
winner = max(bids, key=bids.get)
print(f"The winner is {winner} with a bid of ${bids[winner]}.")
```



### 📂 Day 10: Functions with Outputs

**Topic:** Return Statements, Docstrings, and the Calculator Project

Today, I explored how to get data out of functions using the `return` keyword. I also learned how to document code properly with docstrings and how to store functions inside dictionaries to build a modular calculator.

#### 🗝️ Key Concepts

* **Return Values:** Unlike `print()`, which just shows a value, `return` sends data back to the caller so it can be stored in a variable or used in further calculations.
* **Docstrings:** Using triple quotes `""" """` on the first line after a function definition to provide documentation. This information appears when you hover over the function call.
* **Early Returns:** Using a `return` statement to exit a function early if certain conditions are met (e.g., if a user provides invalid input).
* **Functions as Values:** Storing functions in a dictionary (e.g., `operations = {"+": add}`) allows the program to call specific functions based on user input without using a long chain of `if/elif` statements.
* **String Formatting:** Using `.title()` to automatically convert strings to "Title Case" (e.g., "masoud mashayekh" → "Masoud Mashayekh").

#### 🛠️ Code Snippets
```python
# Functions in a Dictionary
def add(n1, n2):
    """Adds two numbers together."""
    return n1 + n2

def multiply(n1, n2):
    return n1 * n2

operations = {
    "+": add,
    "*": multiply,
}

num1 = 10
num2 = 5
# Accessing the function via the key and calling it
function = operations["+"]
result = function(num1, num2) 
print(result) # Output: 15

# Leap Year Checker Logic
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
```




### 📂 Day 11: Blackjack Capstone Project

**Topic:** Logic Integration and Complexity Management

Today was a milestone project: building a complete, playable Blackjack game from scratch. This project required combining almost every concept learned so far, including functions with outputs, while loops, global/local scope, and advanced list manipulation.

#### 🗝️ Key Concepts

* **Card Representation:** Using a list of integers to represent a standard deck `[11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]`.
* **The "Ace" Logic:** Handling the dual value of the Ace (11 or 1). If the score exceeds 21, the code checks for an 11 and converts it to a 1.
* **Modular Functionality:**
    * `deal_card()`: Uses `random.choice()` to return a card.
    * `calculate_score()`: Checks for a Blackjack (Ace + 10) or adjusts for Aces.
    * `compare()`: Contains the win/loss/draw logic based on final scores.
* **Dealer AI:** Implementing the rule where the computer must keep drawing cards until its score is at least 17.
* **Game State Management:** Using a main `play_game()` function and a recursive `while` loop to allow the user to restart the game and clear the console between rounds.

#### 🛠️ Code Snippets
```python
def calculate_score(cards):
    """Takes a list of cards and returns the score calculated from the cards"""
    # Check for Blackjack (Ace + 10-value card)
    if sum(cards) == 21 and len(cards) == 2:
        return 0 
    
    # Check for an 11 (Ace). If score > 21, replace 11 with 1.
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
        
    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"
```




### 📂 Day 12: Scope & The Number Guessing Game

**Topic:** Local vs. Global Scope and Namespace Management

Today, I explored how Python determines the reach of variables and how to manage them using scope. I learned the difference between global and local namespaces and built a logic-based "Number Guessing Game."

#### 🗝️ Key Concepts

* **Scope:** Defines where a variable can be seen or used.
    * **Global Scope:** Variables defined outside of functions. They are accessible anywhere in the file.
    * **Local Scope:** Variables defined inside a function. They only exist within that function.
* **The `global` Keyword:** Used to modify a global variable from inside a local function. *Best Practice:* Use this sparingly as it can make debugging difficult.
* **No Block Scope:** Unlike many other languages, Python blocks like `if`, `for`, or `while` do **not** create a new scope. Variables defined inside these blocks are still accessible outside them.
* **Global Constants:** Variables that are intended to never change. By convention, these are written in `ALL_UPPERCASE` (e.g., `PI = 3.14159`).
* **Namespace:** A system to ensure that names in a program are unique and can be used without conflict.

#### 🛠️ Code Snippets
```python
# Modifying Global Scope
enemies = 1

def increase_enemies():
    global enemies # Explicitly tell Python we mean the global variable
    enemies += 1
    print(f"Enemies inside function: {enemies}")

increase_enemies()

# Global Constants Convention
URL = "[https://www.google.com](https://www.google.com)"
MAX_SCORE = 100

def check_score():
    if player_score > MAX_SCORE:
        print("New Record!")
```



### 📂 Day 13: Debugging in Python 🐞

**Topic:** The Art of Finding and Fixing Code Errors

Debugging is a core programming skill. It is the process of finding errors, understanding why they occur, and fixing them without breaking other parts of the program. Today was about learning the mindset and the tools used to squish bugs effectively.

#### 🗝️ Top 10 Debugging Strategies

*   **Describe the Problem:** Before changing code, understand exactly what it *should* do vs. what it *is* doing. For example, realizing that `range(1, 20)` excludes 20 helps fix loops that stop too early.
*   **Reproduce the Bug:** Make the bug happen consistently. If a list has 6 items, testing with `randint(1, 6)` might cause an **IndexError** because lists start at index 0. You must reproduce this to verify the fix.
*   **Play Computer:** Step through the code line-by-line in your head or on paper. Evaluate "edge cases"—what happens exactly at the boundary of an `if` statement (e.g., if a user is exactly 1994 years old)?
*   **Handle Exceptions:** Use `try / except` blocks to catch errors like `ValueError` when a user enters text instead of a number. This prevents the entire program from crashing.
*   **Print is your BFF:** Use `print()` statements to "see" inside variables. It helps identify if you used a comparison operator `==` instead of an assignment operator `=` by mistake.
*   **Use a Debugger:** Use software tools (like those in VS Code or PyCharm) to pause execution, inspect the current state of all variables, and "step into" complex functions.
*   **Take a Break:** When logic blurs, step away from the screen. A fresh brain often spots invisible mistakes in seconds.
*   **Ask a Friend:** Explaining your code to someone else helps you spot your own assumptions. If no one is around, try "Rubber Duck Debugging" by explaining it to an object.
*   **Run Code Often:** Don't write 100 lines and then test. Write a small block, run it, fix it, and repeat. This prevents compound bugs that are harder to trace.
*   **Consult Stack Overflow:** If you encounter a specific error message, search for it. Chances are, another developer has already solved the exact same problem.

#### 🛠️ Code Snippets

```python
# 1. Handling User Input Errors
try:
    age = int(input("How old are you? "))
except ValueError:
    print("Invalid input. Please enter a numerical value.")
    age = int(input("How old are you? "))

# 2. Playing Computer: Checking Edge Cases
year = int(input("What's your birth year? "))
if year > 1980 and year <= 1994: # Checking the boundary of 1994
    print("You are a millennial.")
elif year > 1994:
    print("You are a Gen Z.")
```



### 📂 Day 14: Higher or Lower Game 🎮

**Topic:** Capstone Project - Logic Integration & State Management

Today was the final Capstone project of the "Beginner" section. I built a "Higher or Lower" follower comparison game that required integrating dictionaries, nested loops, and global state management into a clean, professional program structure.

#### 🗝️ Key Concepts

*   **Realistic Data Structures:** Working with a large list of dictionaries where each item contains multiple keys (name, follower count, description, country).
*   **Winner Stays Logic:** A key challenge was ensuring that if the player guesses correctly, the "winner" of the previous round becomes the new "Account A," while a new "Account B" is generated.
*   **Data Formatting:** Creating a helper function `format_data()` to parse dictionary values into a user-friendly string, keeping the main game logic uncluttered.
*   **Game State Control:** Using a `while` loop driven by a boolean flag (`continue_game`) and maintaining a running `score` variable throughout the session.
*   **Input Validation:** Handling user guesses and ensuring the game provides immediate feedback before moving to the next round.

#### 🛠️ Code Snippets
```python
# Helper function to format dictionary data into printable text
def format_data(account):
    """Takes the account data and returns a printable format."""
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"

# Core Logic: Checking the guess and updating the game state
if user_guess == "A" and account_a["followers_count"] > account_b["followers_count"]:
    score += 1
    print(f"You're right! Current score: {score}")
    # Account B is replaced for the next round
    account_b = random.choice(instagram_data)
elif user_guess == "B" and account_b["followers_count"] > account_a["followers_count"]:
    score += 1
    print(f"You're right! Current score: {score}")
    # Account A is replaced by the winner (B)
    account_a = account_b
    account_b = random.choice(instagram_data)
else:
    print(f"Sorry, that's wrong. Final score: {score}")
    continue_game = False
```




### 📂 Day 15: 

**Topic:**


### 📂 Day 16: 

**Topic:**

### 📂 Day 17: 

**Topic:**

### 📂 Day 18: 

**Topic:**

### 📂 Day 19: 

**Topic:**

### 📂 Day 20: 

**Topic:**

### 📂 Day 21: 

**Topic:**

### 📂 Day 22: 

**Topic:**

### 📂 Day 23: 

**Topic:**

### 📂 Day 24: 

**Topic:**

### 📂 Day 25: 

**Topic:**


### 📂 Day 26: 

**Topic:**

### 📂 Day 27: 

**Topic:**

### 📂 Day 28: Tkinter, Dynamic Typing and the Pomodoro GUI Application

**Topic:** Pomodoro GUI Application


