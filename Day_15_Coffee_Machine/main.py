# Coffee Machine
from menu import resources, menu

# 1 
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

# 2
def check_ingredients(user_request):
    '''Returns True when order can be made, False if ingredients are insuffucuent.'''
    for i in menu[user_request]["ingredients"]:
        if resources[i] < menu[user_request]["ingredients"][i]:
            print(f"Sorry there is not enough {i}.")
            return False
    return True

# 3
def input_coins():
    '''Returns the total calculated from coins inserted.'''
    print("Please insert coins.")
    total = float(input("How many penny?: ")) * 0.01
    total += float(input("How many nickel?: ")) * 0.05
    total += float(input("How many dime?: ")) * 0.1
    total += float(input("How many quarter?: ")) * 0.25
    return total

# 4
def is_transaction_successful(payment,drink_cost,user_request):
     if payment >= drink_cost:
        remain = payment - drink_cost
        resources["money"] += drink_cost
        print(f"Here is your ${round(remain,2)} in change.")
        print(f"Here is your {user_request} Enjoy!☕️")
        use_ingredients(user_request)
     else:
        print("Sorry that's not enough money. Money refunded.")

# 5
def use_ingredients(user_request):
    for i in menu[user_request]["ingredients"]:
        resources[i] -= menu[user_request]["ingredients"][i]

# 6 
def check_resources():
    print(f"Water: {resources["water"]} ml")
    print(f"Milk: {resources["milk"]} ml")
    print(f"Coffee: {resources["coffee"]} g")
    print(f"Money: $ {resources["money"]}")

# 7
def coffee_machine():
    machine_off = True
    while machine_off:
        user_request = user_input()    
        if user_request == "Report":
            check_resources()
        elif user_request in menu:
            if not check_ingredients(user_request):
                pass
            else:    
                payment = input_coins()
                drink_cost = menu[user_request]["price"]
                is_transaction_successful(payment,drink_cost,user_request)
        else:
            print("See you soon!")
            machine_off = False
            



coffee_machine()         
