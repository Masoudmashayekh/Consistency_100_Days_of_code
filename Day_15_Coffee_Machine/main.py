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

def check_resources():
    print(f"Water: {resources["water"]} ml")
    print(f"Water: {resources["milk"]} ml")
    print(f"Water: {resources["coffee"]} ml")
    print(f"Money: $ {resources["money"]}")
    
def check_ingredients(user_request):
    for i in menu[user_request]["ingredients"]:
        if resources[i] >= menu[user_request]["ingredients"][i]:
            return True
        else:
            print(f"Sorry there is not enough {i}.")


def input_coins():
    penny = float(input("How many penny?: "))
    nickel = float(input("How many nickel?: "))
    dime = float(input("How many dime?: "))
    quarter = float(input("How many quarter?: "))
    total_money = (penny * 0.01) + (nickel * 0.05) + (dime * 0.1) + (quarter * 0.25)
    return total_money

def user_input():
    correct_input = False
    allowable_answers = ["Report", "Espresso", "Latte", "Cappuccino", "Off"]
    while not correct_input:
        request = input("What would you like? (espresso/latte/cappuccino): ").capitalize()
        if request not in allowable_answers: 
            print("Please enter correct input")
        else:
            correct_input = True
            return request





user_request = user_input()
      
if user_request == "Report":
    check_resources()
elif user_request == "Espresso":
    check_ingredients(user_request)
    
            
