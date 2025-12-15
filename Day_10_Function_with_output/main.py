# More about Functions
# Function with input
# Function with output
# def my_function():
#   return 3 * 2
# Docstrings => First line after function ''' Text '''

# what is your first number? 
# +
# -
# *
# /
# Pick an operation: 
# What is the next number?
# 
# Type 'y' to continue calculating with 15 or type 'n' to start new calculation: y
# +
# -
# *
# /
# Pick an operation:
# What is the next number?


def add(n1, n2):
    ''' Add numbers'''
    return n1 + n2

def subtract(n1, n2):
    ''' Subtract numbers'''
    return n1 - n2

def multiply(n1, n2):
    ''' Multiply numbers'''
    return n1 * n2

def divide(n1, n2):
    ''' Divide numbers'''
    return n1 / n2

operations = { "+" : add, "-" : subtract, "*" : multiply, "/" : divide}

should_accumulate = True
num1 = float(input("what is your first number? "))
for symbol in operations:
    print(symbol)
operation_symbol = input("Pick an operation: ")
num2 = float(input("What is the next number? "))
answer = operations[operation_symbol](num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")
choice = input(f"Type 'y' to continue calculating with {answer} or type 'n' to start new calculation: ")
if choice == "y":
    num1 == answer