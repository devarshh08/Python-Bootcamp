from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
is_on = True

while is_on == True:
    coffees = menu.get_items()
    choice = input(f"What coffee would you like? {coffees}\n")
    if choice == "report":
        coffee_maker.report()
    
    elif choice == "off":
        is_on = False

    # elif choice == "refill":
    #     refill = input("What would you like to refill: ")
    #     refill_amt = int(input("How much would you like to refill? "))
    #     if refill in coffee_maker.resources():
    #         coffee_maker.resources[refill] += refill
    
    """This would've worked, but dictionary is not mutable🤷‍♂️"""

    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)