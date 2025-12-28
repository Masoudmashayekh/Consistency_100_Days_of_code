from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffeemaker = CoffeeMaker()
moneymachine = MoneyMachine()

print(menu.get_items())
print(menu.find_drink("latte"))
print(coffeemaker.report())
print(coffeemaker.is_resource_sufficient)
print(moneymachine.report())

user_order = input(f"What would you like to drink? {menu.get_items()}")
drink_name = menu.find_drink(user_order).name
drink_cost = menu.find_drink(user_order).cost
drink_ingredients = menu.find_drink(user_order).ingredients
print(drink_cost)
print(drink_ingredients)
print(drink_name)