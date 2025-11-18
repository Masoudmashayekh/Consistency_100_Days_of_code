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

# print("Welcome!")
# height = int(input("What is your height cm? "))
# age = int(input("How old are you?"))
# if height >= 120:
#     if age <= 12:
#         print("Can Ride and pay 5$")
#     elif 12 < age <= 18:
#         print("Can Ride and pay 7$")
#     else:
#         print("Can Ride and pay 12$")
# else:
#     print("Can not Ride")
    


weight = 85
height = 1.85

bmi = weight / (height ** 2)

# 🚨 Do not modify the values above
# Write your code below 👇

if bmi <= 18.5:
    print("underweight")
elif 18.5 < bmi < 25:
    print("normal weight")
else:
    print("overweight")


# Multiple if

print("Welcome!")
height = int(input("What is your height cm? "))
age = int(input("How old are you?"))
bill = 0
if height >= 120:
    if age <= 12:
        bill = 5
        print("Can Ride and pay 5$")
    elif 12 < age <= 18:
        bill = 7
        print("Can Ride and pay 7$")
    else:
        bill = 12
        print("Can Ride and pay 12$")
    wants_photo = input("Do you want to have a photo take? Type y for Yes and n for No.")
    if wants_photo == "y":
        bill += 3
    print(f"Your final bill is {bill} $")
else:
    print("Can not Ride")