from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from prettytable import PrettyTable



# Create all the objects
table = PrettyTable()
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
on = True
# print(menu.find_drink("latte").cost)
# Print a pretty menu.
table.field_names = ["Name", "Price"]
items = menu.get_items().split('/')
# Solve that fence post problem of the empty string at the end.
items.pop()
for item in items:
    price = menu.find_drink(item).cost
    table.add_row([item, "$" + "{:.2f}".format(price)])
table.align = "l"

while on:
    print(table)
    drink = input(f"Please select from the menu above.\n")
    if drink not in menu.get_items():
        print("Please select a valid input")
    elif drink == "off":
        on = False
    elif drink == "report":
        print(coffee_maker.report())
    else:
        drink = menu.find_drink(drink)
        # Check Resources Sufficient. If not enough then empty is True.
        empty = not coffee_maker.is_resource_sufficient(drink)

        # Check Transaction Successful
        poor = not money_machine.make_payment(drink.cost)
        # Make Coffee
        if not empty and not poor:
            coffee_maker.make_coffee(drink)