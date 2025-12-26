# Coffee Machine



# Process coins
# Check transaction successful?
# Make Coffee



# Here is your $ in change.
# Here is your latte Enjoy!
# Sorry there is not enough water.
# Please insert coins.
# How many quarters?: 
menu = {
    "Espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18
        },
        "price": 1.5
    },
    "Latte": {
        "ingredients": {
            "water": 200,
            "coffee": 24,
            "milk": 150
        },
        "price": 2.5
    },
    "Cappuccino": {
        "ingredients": {
            "water": 250,
            "coffee": 24,
            "milk": 100
        },
        "price": 3.0
    }
}

resources = {
    "water": 300,
    "coffee": 100,
    "milk": 200,
    "money": 0,
}

def check_resources():
    print(f"Water: {resources["water"]} ml")
    print(f"Milk: {resources["milk"]} ml")
    print(f"Coffee: {resources["coffee"]} ml")
    print(f"Money: $ {resources["money"]}")
    
def check_ingredients(user_request):
    for i in menu[user_request]["ingredients"]:
        if resources[i] >= menu[user_request]["ingredients"][i]:
            return True
        else:
            print(f"Sorry there is not enough {i}.")
            return False

def use_ingredients(user_request):
    for i in menu[user_request]["ingredients"]:
        resources[i] -= menu[user_request]["ingredients"][i]
        


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




machine_off = True
while machine_off:
    user_request = user_input()    
    if user_request == "Report":
        check_resources()
    elif user_request in menu:
        if not check_ingredients(user_request):
            pass
        else:    
            coins = input_coins()
            if coins >= menu[user_request]["price"]:
                remain = coins - menu[user_request]["price"]
                resources["money"] += menu[user_request]["price"]
                print(f"Here is your ${remain} in change.")
                print(f"Here is your {user_request} Enjoy!")
                use_ingredients(user_request)
            else:
                print("Sorry that's not enough money. Money refunded.")
    else:
        print("See you soon!")
        machine_off = False
        
        
        
                
