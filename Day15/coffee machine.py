MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}


water = 300
milk = 200
coffee = 100
money = 0

def paisa_de():
    quarters = 0
    dimes = 0
    nickels = 0
    pennies = 0
    quarters_taken = float(input("How many quarters? "))
    quarters += quarters_taken*0.25
    dimes_taken = float(input("How many dimes? "))
    dimes += dimes_taken*0.1
    nickels_taken = float(input("How many nickels? "))
    nickels += nickels_taken *0.05
    pennies_taken = float(input("How many pennies? "))
    pennies += pennies_taken*0.01
    given_money = quarters+dimes+nickels+pennies
    refund = given_money - price
    refund = round(refund,2)
    if given_money > price:
        print(f"Here is your {refund} change.")
        print(f"Here is your {user_ch}☕. Enjoy!")
    elif given_money == price:
        print(f"Here is your {user_ch}☕. Enjoy!")
    else:
        print("Insufficient money, Money refunded.")

machine_off = False

while not machine_off:
    user_ch = input("What would you like?\n1. espresso\n2. latte\n3. cappuccino: ")
    if user_ch == "1" or user_ch == "espresso":
        espresso = MENU["espresso"]
        ingredients = espresso["ingredients"]
        water_needed = ingredients["water"]
        coffee_needed = ingredients["coffee"]
        if coffee < coffee_needed or water < water_needed:
            print("Insufficient ingredients")
        else:
            water -= water_needed
            coffee -= coffee_needed
            price = espresso["cost"]
            money += price
            print(f"The price of espresso coffee is {price}")
            paisa_de()
        

    elif user_ch == "2" or user_ch == "latte":
        latte = MENU["latte"]
        ingredients = latte["ingredients"]
        water_needed = ingredients["water"]
        coffee_needed = ingredients["coffee"]
        milk_needed = ingredients["milk"]
        if coffee < coffee_needed or water < water_needed or milk < milk_needed:
            print("Insufficient ingredients")
        else:
            water -= water_needed
            coffee -= coffee_needed
            milk -= milk_needed
            price = latte["cost"]
            money += price
            print(f"The price of latte coffee is {price}")
            paisa_de()

    elif user_ch == "3" or user_ch == "cappuccino":
        cappuccino = MENU["cappuccino"]
        ingredients = cappuccino["ingredients"]
        water_needed = ingredients["water"]
        coffee_needed = ingredients["coffee"]
        milk_needed = ingredients["milk"]
        if coffee < coffee_needed or water < water_needed or milk < milk_needed:
            print("Insufficient ingredients")
        else:
            water -= water_needed
            coffee -= coffee_needed
            milk -= milk_needed
            price = cappuccino["cost"]
            money += price
            print(f"The price of cappuccino coffee is {price}")
            paisa_de()

    elif user_ch == "report":
        print(f'''water = {water}\nmilk = {milk}\ncoffee = {coffee}\nmoney = {money}\n''')

    elif user_ch == "refill water":
        water_refill = int(input("How much water would you like to refill: "))
        water += water_refill
    
    elif user_ch == "refill water":
        coffee_refill = int(input("How much coffee would you like to refill: "))
        coffee += coffee_refill
    
    elif user_ch == "refill milk":
        milk_refill = int(input("How much milk would you like to refill: "))
        milk += milk_refill
    
    elif user_ch == "off":
        machine_off = True
        break
    