# ☕ Premium Coffee Machine - Python Project

A functional terminal-based coffee machine built with Python.  
It simulates a real coffee vending machine, handling ingredient resources, coin transactions, and multiple drink options.



---

## 🚀 Features

- Interactive command-line interface
- Accepts coins and calculates total payment
- Provides change if overpaid
- Tracks available resources (water, milk, coffee)
- Prevents transaction if ingredients are insufficient
- Supports turning off the machine with `"off"` command
- Detailed report generation via `"report"` command

---

## 🧠 Menu & Recipes

Each drink has its own ingredients and cost:

| Drink       | Water (ml) | Milk (ml) | Coffee (g) | Cost ($) |
|-------------|------------|-----------|------------|----------|
| Espresso    | 50         | -         | 18         | 1.50     |
| Latte       | 200        | 150       | 24         | 2.50     |
| Cappuccino  | 250        | 100       | 24         | 3.00     |

---

## 💵 Supported Coins

- Quarters: `$0.25`
- Dimes: `$0.10`
- Nickels: `$0.05`
- Pennies: `$0.01`

Users are asked how many of each coin they insert.  
The machine will calculate the total and determine if it's sufficient.

---

## 🖥️ How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/JeremyPanggabean/coffee-machine.git
2. Change the directory:
   ```bash
   cd coffee-machine
3. Run the script:
   ```bash
   python coffee_machine.py


## Sample Session
   ```bash
   
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
    
What would you like? (espresso/latte/cappuccino): espresso
Please insert coins.
How many quarters?: 6
How many dimes?: 4
How many nickles?: 5
How many pennies?: 3
Customer inserted: $2.18
Here is $0.68 in change.
Here is your espresso ☕. Enjoy!

What would you like? (espresso/latte/cappuccino): latte
Please insert coins.
How many quarters?: 10
How many dimes?: 11
How many nickles?: 8
How many pennies?: 7
Customer inserted: $4.07
Here is $1.57 in change.
Here is your latte ☕. Enjoy!

What would you like? (espresso/latte/cappuccino): report
Water: 2750ml
Milk: 1850ml
Coffee: 958g
Money: $4.0

What would you like? (espresso/latte/cappuccino): cappuccino
Please insert coins.
How many quarters?: 12
How many dimes?: 15
How many nickles?: 11
How many pennies?: 9
Customer inserted: $5.14
Here is $2.14 in change.
Here is your cappuccino ☕. Enjoy!

What would you like? (espresso/latte/cappuccino): milk
Invalid input. Choose: espresso / latte / cappuccino / off

What would you like? (espresso/latte/cappuccino): off
Turning off. Thanks for using the Coffee Machine ☕
