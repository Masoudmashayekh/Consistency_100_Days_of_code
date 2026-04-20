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



