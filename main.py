from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
is_on = True



while is_on:
    options = menu.get_items()
    choice = input(f"What would you like to drink? {options} \nif you don't to proceed type Off " ) .lower()
    if choice == "off":
        is_on = False
    elif choice=="report":
        coffee_maker.report()
        money_machine.report()




