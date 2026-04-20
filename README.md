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


---

### 📂 Day 2: Data Types & String Manipulation
**Topic:** Data Types, Numbers, and f-Strings

*   **Data Types:** `str` (text), `int` (whole numbers), `float` (decimals), `bool` (True/False).
*   **Subscripting:** Access characters using `[index]` (e.g., `"Hello"[0]` is "H").
*   **Type Checking:** Use `type()` to identify a variable's class.
*   **Type Conversion:** Change types using `str()`, `int()`, or `float()`.
*   **Math Operators:** `+`, `-`, `*`, `/`, and `**` for exponents.
*   **Rounding:** `round(number, precision)` for decimal control.
*   **f-Strings:** Easily insert variables into strings: `f"Score: {score}"`.
```python
score = 0
height = 1.8
is_winning = True
print(f"Your score is {score}, your height is {height}, you are winning: {is_winning}")