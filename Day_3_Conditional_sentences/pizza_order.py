small_pizza = 15
medium_pizza = 20
large_pizza = 25
pepperoni_small = 2
pepperoni_l_m = 3
cheese_price = 1
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ").upper()
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").upper()
extra_cheese = input("Do you want extra cheese? Y or N: ").upper()
bill = 0
if size == "S":
    bill += small_pizza
    if pepperoni == "Y":
        bill += pepperoni_small
    if extra_cheese == "Y":
        bill += cheese_price
elif size == "M":
    bill += medium_pizza
    if pepperoni == "Y":
        bill += pepperoni_l_m
    if extra_cheese == "Y":
        bill += cheese_price
elif size == "L":
    bill += large_pizza
    if pepperoni == "Y":
        bill += pepperoni_l_m
    if extra_cheese == "Y":
        bill += cheese_price
else:
    print("You typed the wrong inputs.")

print(f"Your final bill is: ${bill}.")

    