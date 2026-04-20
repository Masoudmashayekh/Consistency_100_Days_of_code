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