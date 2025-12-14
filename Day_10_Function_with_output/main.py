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


first_number = float(input("what is your first number? "))
continue_ = True
while continue_:
    pick_operation = input(f"+\n-\n*\n/\nPick an operation: ")
    second_number = float(input("What is the next number?"))
    final_result = operations[pick_operation](first_number, second_number)
    print(final_result)
    continue_or_not = input("Type 'y' to continue calculating with 15 or type 'n' to start new calculation: ")
