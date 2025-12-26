# Coffee Machine
# Makes 3 hot flavours

# Espresso  50ml water, 18g Coffee, $1.5
# Latte 200mk Water, 24g Coffee, 150ml Milk, $2.5
# Cappuccino 250ml Water, 24g Coffee, 100ml Milk, $3

# Machine 300ml Water, 200ml Milk, 100g Coffee

# 2. Coin Operated: Penny: 1 cent, Nickel: 5 cents, Dime: 10 cents, Quarter: 25 cents, 0.01, 0.05, 0.10, 0.25

# Print Report
# Check resources sufficient?
# Process coins
# Check transaction successful?
# Make Coffee


# What would you like? (espresso/latte/cappuccino): report
# Water: 300 ml
# Milk: 200 ml
# Coffee: 100 g
#Money: $0
# Here is your $ in change.
# Here is your latte Enjoy!
# Sorry there is not enough water.
# Please insert coins.
# How many quarters?: 
# Sorry that's not enough money. Money refunded.

from menu import resources, menu

def check_resources(money):
    print(f"Water: {resources["water_ml"]} ml")
    print(f"Water: {resources["milk_ml"]} ml")
    print(f"Water: {resources["coffee_g"]} ml")
    print(f"Money: $ {money}")

def coins():
    penny = float(input("How many penny?: "))
    nickel = float(input("How many nickel?: "))
    dime = float(input("How many dime?: "))
    quarter = float(input("How many quarter?: "))
    total_money = (penny * 0.01) + (nickel * 0.05) + (dime * 0.1) + (quarter * 0.25)
    return total_money

def user_input():
    correct_input = False
    allowable_answers = ["report", "espresso", "latte", "cappuccino", "off"]
    while not correct_input:
        request = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if request not in allowable_answers: 
            print("Please enter correct input")
        else:
            correct_input = True
            return request



money = 0

user_request = user_input()
        
if user_request == "report":
    check_resources(money)
elif user_request == "espresso":
    pass
