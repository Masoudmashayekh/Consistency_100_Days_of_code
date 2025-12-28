from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

continue_game = True
while continue_game:
    user_order = input(f"What would you like to drink? {menu.get_items()}")
    if user_order == "report":
        coffee_maker.report()
        money_machine.report()
    elif user_order == "off":
        print("See you later. Bye!")
        continue_game = False
    else:
        drink_name = menu.find_drink(user_order)
        if coffee_maker.is_resource_sufficient(drink_name) and money_machine.make_payment(drink_name.cost):
            coffee_maker.make_coffee(drink_name)