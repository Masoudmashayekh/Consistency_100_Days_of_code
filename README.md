Day 1
Print output: Use print() to display text or instructions.


Strings: Enclosed in " " or ' '. Combine with +. Use \n for new lines.


Comments: Start with # to explain code.


Variables: Store data, e.g., name = "Hello". Use len() to get string length.


User Input: input() gets data from the user as a string.


Errors:


IndentationError → wrong spacing


SyntaxError → invalid code















Day 2
Data Types: Python has 4 main types — str, int, float, bool.
Strings (str):
 Text inside quotes " ".
 Use indexing [ ] to get characters → "Hello"[0] → H.
 Combine with + → "123" + "456" → "123456".
Integers (int):
 Whole numbers → 123, 456.
 Use _ for readability → 1_000_000.
Floats (float):
 Numbers with decimals → 3.14.
Booleans (bool):
 Only True or False.
Type Checking:
 Use type() → type(123) → <class 'int'>.
Type Conversion:
 Convert between types → int("123") or str(123).
Math Example (BMI):
 bmi = 84 / 1.65 ** 2
 round(bmi, 2) → round to 2 decimals.
Shorthand Operators:
 +=, -=, *=, /= to update variable values.
f-Strings:
 Insert variables into strings easily →
 f"Your score is {score}, your height is {height}m."












Day 3 - Conditional Statements in Python
Conditional Statements:
 Use if, elif, and else to make decisions in your code.
 Python checks conditions from top to bottom.
if condition:
    # run this code
else:
    # run this instead
Example:
if 120 >= 100:
    print("Allowed")
else:
    print("Not allowed")
Comparison Operators:
 > greater than
 < less than
 >= greater or equal
 <= less or equal
 == equal to
 != not equal
 = assigns a value (not a comparison)
Modulo Operator %:
 Returns the remainder after division.
 10 % 2 → 0 (even)
 10 % 3 → 1 (odd)
 Used to check even/odd numbers.

If / Elif / Else:
 if → first condition
 elif → additional condition(s)
 else → runs only if all above conditions are false
 Example:
bmi ≤ 18.5 → underweight


18.5 < bmi < 25 → normal


else → overweight


Nested Conditions:
 An if inside another if.
 Allows multi-step decisions.
 Example:
Check height


If tall enough, check age


Choose ticket price based on age


Multiple If Statements:
 All conditions are tested, not just one.
 Used when multiple things can be true.
 Example:
add pepperoni


add cheese


add photo
 Each option updates the bill separately.


Logical Operators:
 and → both conditions must be true
 or → at least one true
 not → reverses True/False
 Example:
 age >= 45 and age <= 55 → free ride zone

Input Handling:
 .upper() → converts response to uppercase (Y/N)
 .capitalize() → makes first letter uppercase (Left/Right)

Mini Projects Covered:
 BMI Program:
 Uses if/elif/else to classify BMI.
Rollercoaster Program:
 Height check, age-based pricing, optional photo, logic with and.
Pizza Order:
 Size selection, pepperoni choice, extra cheese, running total with multiple ifs.
Treasure Island Game:
 Interactive story using nested decisions until win or game over.



Day 4 – Python Random, Modules & Lists
Random
random.randint(a,b) → random integer a ≤ x ≤ b


random.random() → float 0 ≤ x < 1


random.uniform(a,b) → float a ≤ x ≤ b


random.choice(list) → pick random item from a list


Example – Coin toss:
if random.randint(0,1) == 0:
    print("Heads")
else:
    print("Tails")
Modules
Import custom or built-in modules:


import my_module
print(my_module.my_favorite_number)
Lists & Nested Lists
Regular list: fruits = ["Apple", "Banana"]


Nested list: dirty_dozen = [fruits, vegetables]


Access: dirty_dozen[0][1] # Banana


Add items: states.append("Masoud_land")


Mini Example – Rock Paper Scissors
list = ["Rock","Paper","Scissors"]
pc = random.choice(list)
me = list[int(input("0=Rock,1=Paper,2=Scissors: "))]
if me == pc: print("Draw")
elif (me=="Rock" and pc=="Scissors") or (me=="Paper" and pc=="Rock") or (me=="Scissors" and pc=="Paper"): print("You win!")
else: print("You lose!")


