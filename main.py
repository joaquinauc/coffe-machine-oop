from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu_coffee_machine = Menu()
coffee_machine = CoffeeMaker()
money_coffee_machine = MoneyMachine()

is_on = True

while is_on:
    choice = input(f"What would you like? ({menu_coffee_machine.get_items()})\n")
    if choice == "report":
        coffee_machine.report()
        money_coffee_machine.report()
    elif choice == "off":
        is_on = False
    else:
        drink = menu_coffee_machine.find_drink(choice)
        # drink is an object as menu_coffee_machine.find_drink(choice) is basically a class
        # because it is equal to a menu item (MenuItem).
        if coffee_machine.is_resource_sufficient(drink):
            if money_coffee_machine.make_payment(drink.cost):
                coffee_machine.make_coffee(drink)
