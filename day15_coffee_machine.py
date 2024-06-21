from art import coffee, coffee_machine
from menu import MENU
import math

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

machine_money = 0

def show_prices():
    print(f"""
Coffee Machine prices:
Espresso: ${MENU["espresso"]["cost"]:.2f}
Latte: ${MENU["latte"]["cost"]:.2f}
Cappuccino: ${MENU["cappuccino"]["cost"]:.2f}""")


def show_report():
    print(f"""Water: {resources['water']}ml
Milk: {resources['milk']}ml
Coffee: {resources['coffee']}ml
Money: ${machine_money:.2f}""")


def check_resources(drink):
    """Takes a drink request and checks if the machine has the resources to make said drink.
    Checks whether it's empty or not."""
    ingredients = MENU[drink]["ingredients"]
    for element in ingredients:
        if ingredients[element] > resources[element]:
            print(f"Low {element}.")
            return True
    return False


def process_coins(drink):
    """Process the coins based on the drink and return the change.
    If they don't have enough money, refund them and return -1 from the function."""
    dollars = int(input("How many dollars? "))
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))
    given_money = dollars + quarters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01
    cost = MENU[drink]["cost"]
    # Process whether they have enough money here. 
    if cost > given_money:
        print(f"Not enough money. Your change is ${given_money:.2f}.")
        return -1
    else: # cost <= given_money. Keep the cost of the drink and return their change.
        return round(given_money - cost, 2)


def make_coffee(drink):
    """Remove the ingredients for the drink from the resources."""
    ingredients = MENU[drink]["ingredients"]
    for element in ingredients:
        resources[element] -= ingredients[element]
    print(f"Here is your {drink}. Enjoy!")


thirsty = True
while thirsty:
    change = 0
    # Print prices.
    show_prices()
    # Get input.
    request = input("What would you like? (espresso/latte/cappuccino): ")
    # request = "espresso"
    if request == "report":
        show_report()
    elif request == "off":
        thirsty = False
    else:
        # Check resources sufficient compared to what's being ordered.
        empty = check_resources(request)
        if not empty:
            # Process coins. Check that you have enough money.
            change = process_coins(request)
        # Check if poor by getting a negative number
        poor = False
        if change < 0:
            poor = True
            print("I'm poor")
        # Only make coffee if they had enough to buy it.
        if not poor and not empty:
            # Money goes to the machine.
            print(f"Your change is ${change:.2f}.")
            machine_money = machine_money + MENU[request]["cost"]
            # Make coffee.
            make_coffee(request)
        elif not poor and empty:
            print("Not enough resources to make your drink.")