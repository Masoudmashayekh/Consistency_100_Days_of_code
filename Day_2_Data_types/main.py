# Strings, integer, float, boolean
# Strings   "Hello"
print("Hello"[0]) # Subscripting the string to get 'H'
print("Hello"[4]) # Subscripting the string to get 'o'
print("Hello"[-1]) # Subscripting the string to get 'o'

# "123" is a string, str
print("123" + "456")


# Integer = Whole number, int
print(123 + 456)

# Large integer : The underscores (_) make large numbers easier to read in Python.
print(123_345_546_333)

# Float = Floating-point number, float
print(3.14159)

# Boolean = True or False, bool
print(True)
print(False)

# type checking
print(type(123)) # <class 'int'>
print(type(3.14)) # <class 'float'>
print(type("Hello")) # <class 'str'>
print(type(True)) # <class 'bool'>

# Type conversion
print(int("123") + int("456"))

# print("Number of letters: " + str(len(input("What is the name?"))))


bmi = 84 / 1.65 ** 2
print(bmi)
print(int(bmi))
print(round(bmi)) # for rounding numbers. # 30
print(round(bmi, 2)) # 30.85


#  +=  -= *= /=
score = 0
score +=10
print(score)
height = 1.86
is_winning = True

# f-string
print(f"Your score is {score}, your height is {height}m, You are winning is {is_winning}.")