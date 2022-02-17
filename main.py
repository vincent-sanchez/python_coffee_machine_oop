# Import classes/packages
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Declare global variables
play = True

# Instantiate objects
menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

# Play Coffee Machine
while(play):
    drink_order = input(f"What would you like? {menu.get_items()}: ")
    if drink_order == 'off':
        print("Powering down the coffee machine!")
        play = False
    elif drink_order == 'report':
        coffee_maker.report()
        money_machine.report()
    elif menu.find_drink(drink_order) is None:
        None
    else:
        order = menu.find_drink(drink_order)
        if not coffee_maker.is_resource_sufficient(order):
            play = False
        else:
            money_machine.make_payment(order.cost)
            coffee_maker.make_coffee(order)
exit(0)
