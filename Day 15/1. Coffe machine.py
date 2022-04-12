

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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

#TODO 1: 1. Prompt user by asking "What would you like? (espresso/latte/cappuccino):”
prompt = input("What would you like? (espresso/latte/cappuccino): ")

#TODO 2: a. Check the user’s input to decide what to do next.
if prompt=="espresso":
    print(f"You have selected {prompt}")
elif prompt=="latte":
    print(f"You have selected {prompt}")
elif prompt=="cappuccino":
    print(f"You have selected {prompt}")

#TODO 3: b. The prompt should show every time action has completed, e.g. once the drink is dispensed.
# The prompt should show again to serve the next customer.

#TODO 4: 2. Turn off the Coffee Machine by entering “off” to the prompt.
# a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
# the machine. Your code should end execution when this happens.
if prompt=="off":
    print(f"You have selected to turn {prompt}the machine.")

#TODO 6: 3. Print report.
# a. When the user enters “report” to the prompt, a report should be generated that shows
# the current resource values. e.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
water_qty=resources["water"]
milk_qty=resources["milk"]
coffee_qty=resources["coffee"]
money_qty=99
if prompt=="report":
    print(f"Water: {water_qty}ml.")
    print(f"Milk: {milk_qty}ml.")
    print(f"Coffee: {coffee_qty}g.")
    print(f"Money: ${money_qty}.")

#TODO 8: 4. Check resources sufficient?
# a. When the user chooses a drink, the program should check if there are enough
# resources to make that drink.
# b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
# not continue to make the drink but print: “Sorry there is not enough water.”

#TODO 11: c. The same should happen if another resource is depleted, e.g. milk or coffee.

#TODO 12: 5. Process coins.
# a. If there are sufficient resources to make the drink selected, then the program should
# prompt the user to insert coins.
change=0
print("Please insert coins")
quarters=0.25*int(input("how many quarters?: "))
dimes=0.1*int(input("how many dimes?: "))
nickles=0.05*int(input("how many nickles?: "))
pennies=0.01*int(input("how many pennies?: "))
print(f"Here is ${change} in change.")
print(f"Here is your {prompt} ☕️. Enjoy!")
print(quarters)

#TODO 14: b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01

#TODO 15: c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
# pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52
monetary_value=quarters+dimes+nickles+pennies
print(f"monetary value is : {monetary_value}")

#TODO 16: 6. Check transaction successful?
# a. Check that the user has inserted enough money to purchase the drink they selected.
# E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
# program should say “Sorry that's not enough money. Money refunded.”.


#TODO 18: b. But if the user has inserted enough money, then the cost of the drink gets added to the
# machine as the profit and this will be reflected the next time “report” is triggered. E.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5

#TODO 19: c. If the user has inserted too much money, the machine should offer change.E.g. “Here is $2.45 dollars
# in change.” The change should be rounded to 2 decimal places.

#TODO 20: 7. Make Coffee.
# a. If the transaction is successful and there are enough resources to make the drink the
# user selected, then the ingredients to make the drink should be deducted from the
# coffee machine resources.
# E.g. report before purchasing latte:
# Water: 300ml
# Milk: 200ml
# Coffee: 100g
# Money: $0

#TODO 21: Report after purchasing latte:
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5

#TODO 22: b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”.
# If latte was their choice of drink.
