from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffeemaker = CoffeeMaker()
moneymachine = MoneyMachine()

continue_game = True
while continue_game:
    user_order = input(f"What would you like to drink? {menu.get_items()}")
    if user_order == "report":
        coffeemaker.report()
    elif user_order == "off":
        print("See you later. Bey!")
        quit
    else:
        drink_name = menu.find_drink(user_order)
        drink_cost = menu.find_drink(user_order).cost
        drink_ingredients = menu.find_drink(user_order).ingredients
        if coffeemaker.is_resource_sufficient(drink_name):
            if moneymachine.make_payment(drink_cost):
                coffeemaker.make_coffee(drink_name)