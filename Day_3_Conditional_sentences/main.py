# Conditional sentences: if else 
print("Welcome!")
# height = int(input("What is your height cm? "))

# if height >= 120:
#     print("Can Ride")
# else:
#     print("Can not Ride")

# Greater than >
# Less than <
# Greater than or equal to >=
# Less than or equal to <=
# equal to ==
# not equal to !=
# = assigns a value.
# == compares values.

# Modulo Operator %
# 10 % 5 = 0
# 10 % 3 = 1 remaining
print(10 % 3)
print(10 / 3)
# Even number: A number divisible by 2 with no remainder (e.g., 2, 4, 8, 100).
# Odd number: A number that leaves a remainder of 1 when divided by 2 (e.g., 1, 3, 7, 101).

# number = int(input("Enter a number: "))
# if number % 2 == 0 :
#     print("Number is even")
# else:
#     print("Number is odd")
    
    
# Nested if / else
# if / elif / else

print("Welcome!")
height = int(input("What is your height cm? "))
age = int(input("How old are you?"))
if height >= 120:
    if age <= 12:
        print("Can Ride and pay 5$")
    elif 12 < age <= 18:
        print("Can Ride and pay 7$")
    else:
        print("Can Ride and pay 12$")
else:
    print("Can not Ride")
    


