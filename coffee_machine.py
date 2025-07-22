# Menu of drinks with required ingredients and cost
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

# Current available resources in the machine
resources = {
    "water": 3000,
    "milk": 2000,
    "coffee": 1000,
}

# Coin values in dollars
coins = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickles": 0.05,
    "pennies": 0.01
}

# Initial money earned by the machine
money = 0


def welcome_screen():
    print("""
    ☕ WELCOME TO THE PREMIUM COFFEE MACHINE ☕
    
         (  )   (   )  )
          ) (   )  (  (
          ( )  (    ) )
          _____________
         <_____________> ___
         |             |/ _ |
         |   PREMIUM    | | |
         |   COFFEE     |_| |
       __|_______________|___|__
      |_______________________|
    
    🌟 Fresh Coffee • Premium Quality • Fast Service 🌟
    """)


def report():
    """Prints the current resource levels and total money collected."""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${round(money, 2)}")


def is_enough_ingredients(drink):
    """
    Checks if there are enough ingredients for the selected drink.
    Returns True if all ingredients are sufficient, else prints message and returns False.
    """
    for item in MENU[drink]['ingredients']:
        if resources[item] < MENU[drink]['ingredients'][item]:
            print(f"Sorry, not enough {item}.")
            return False
    return True


def process_coins():
    """
    Prompts user to insert coins and calculates the total.
    Returns the total amount inserted, rounded to 2 decimal places.
    """
    print("Please insert coins.")
    total = 0
    for coin in coins:
        count = int(input(f"How many {coin}?: "))
        total += coins[coin] * count
    total = round(total, 2)
    print(f"Customer inserted: ${total}")
    return total


def make_coffee(drink, payment):
    """
    Checks if payment is enough, processes transaction,
    updates resources, adds to money, and serves coffee.
    """
    cost = MENU[drink]["cost"]

    if payment < cost:
        print(f"Sorry, that's not enough money. Money refunded: ${payment}")
        return False

    change = round(payment - cost, 2)
    if change > 0:
        print(f"Here is ${change} in change.")

    # Deduct ingredients from resources
    for item in MENU[drink]["ingredients"]:
        resources[item] -= MENU[drink]["ingredients"][item]

    # Update global money
    global money
    money += cost

    print(f"Here is your {drink} ☕. Enjoy!")
    return True


# Main program loop
machine_on = True
welcome_screen()

while machine_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "off":
        # Turns off the machine
        print("Turning off. Thanks for using the Coffee Machine ☕")
        machine_on = False

    elif choice == "report":
        # Prints current machine status
        report()
        print("")

    elif choice in MENU:
        # Only proceed to payment if ingredients are available
        if is_enough_ingredients(choice):
            payment = process_coins()
            make_coffee(choice, payment)
            print("")
    else:
        print("Invalid input. Choose: espresso / latte / cappuccino / off")
        print("")



