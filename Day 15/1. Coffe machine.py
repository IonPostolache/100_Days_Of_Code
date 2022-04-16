

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

machine_profit=0
change=0
transaction_successful=True


def resources_check(prompt):
    """This function will check the resources"""
    if prompt != "espresso":
        if resources["milk"] - MENU[prompt]["ingredients"]["milk"] >= 0:
            return True
    elif resources["water"] - MENU[prompt]["ingredients"]["water"] >= 0 and resources["coffee"] - \
            MENU[prompt]["ingredients"]["coffee"] >= 0:
        return True
    else:
        print(f"Sorry there is not enough water???.")
        #here I need to replace water with some updatable variable
        return False


def insert_coins():
    """This function will return the total sum inserted """
    print("Please insert coins")
    quarters=0.25*int(input("how many quarters?: "))
    dimes=0.1*int(input("how many dimes?: "))
    nickles=0.05*int(input("how many nickles?: "))
    pennies=0.01*int(input("how many pennies?: "))
    monetary_value = quarters + dimes + nickles + pennies
    print(f"monetary value is : {monetary_value}")
    return monetary_value


def report():
    """This function will print a report of resources"""
    water_qty=resources["water"]
    milk_qty=resources["milk"]
    coffee_qty=resources["coffee"]
    print(f"Water: {water_qty}ml.")
    print(f"Milk: {milk_qty}ml.")
    print(f"Coffee: {coffee_qty}g.")
    print(f"Money: ${machine_profit}.")


def deduction(prompt):
    """This function will manage the resources deduction"""
    #I need to combine deduction() and report() somehow but keep the report clean if asked before the first drink
    water_qty = resources["water"] - MENU[prompt]["ingredients"]["water"]
    if prompt != "espresso":
        milk_qty = resources["milk"] - MENU[prompt]["ingredients"]["milk"]
    coffee_qty = resources["coffee"] - MENU[prompt]["ingredients"]["coffee"]


def money_check(prompt,monetary_value):
    """This function will check if there are enough money and will add the profit"""
    drink_cost = MENU[prompt]["cost"]
    change = monetary_value - drink_cost
    machine_profit=0
    if monetary_value < drink_cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif monetary_value >= drink_cost:
        machine_profit += drink_cost
        print(f"machine profit is: {machine_profit}")
        if monetary_value > drink_cost:
            print(f"Here is ${change} dollars in change.")
        return True


"""def drinks():
    if prompt == "espresso":
        print(f"You have selected {prompt}")
    elif prompt == "latte":
        print(f"You have selected {prompt}")
    elif prompt == "cappuccino":
        print(f"You have selected {prompt}")"""


def main_asking():
    """This is the main function"""
    prompt = input("What would you like? (espresso/latte/cappuccino): ")
    if prompt == "off":
        print(f"You have selected to turn off the machine.")
        return
    elif prompt=="report":
        report()
        main_asking()
    #insert_coins()
    #drinks()
    if resources_check(prompt)==True and money_check(prompt,insert_coins())==True:
        deduction(prompt)
        print(f"Here is your {prompt}. Enjoy!")
    main_asking()

main_asking()

#TODO 1: 1. Prompt user by asking "What would you like? (espresso/latte/cappuccino):”

#TODO 2: a. Check the user’s input to decide what to do next.

#TODO 3: b. The prompt should show every time action has completed, e.g. once the drink is dispensed.
# The prompt should show again to serve the next customer.

#TODO 4: 2. Turn off the Coffee Machine by entering “off” to the prompt.
# a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
# the machine. Your code should end execution when this happens.

#TODO 6: 3. Print report.
# a. When the user enters “report” to the prompt, a report should be generated that shows
# the current resource values. e.g.

#TODO 8: 4. Check resources sufficient?
# a. When the user chooses a drink, the program should check if there are enough
# resources to make that drink.
# b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
# not continue to make the drink but print: “Sorry there is not enough water.”

#TODO 11: c. The same should happen if another resource is depleted, e.g. milk or coffee.

#TODO 12: 5. Process coins.
# a. If there are sufficient resources to make the drink selected, then the program should
# prompt the user to insert coins.

#TODO 14: b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
#TODO 15: c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
# pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52
#TODO 16: 6. Check transaction successful?
# a. Check that the user has inserted enough money to purchase the drink they selected.
# E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
# program should say “Sorry that's not enough money. Money refunded.”.

#TODO 18: b. But if the user has inserted enough money, then the cost of the drink gets added to the
# machine as the profit and this will be reflected the next time “report” is triggered. E.g.

#TODO 19: c. If the user has inserted too much money, the machine should offer change.E.g. “Here is $2.45 dollars
# in change.” The change should be rounded to 2 decimal places.

#TODO 20: 7. Make Coffee.
# a. If the transaction is successful and there are enough resources to make the drink the
# user selected, then the ingredients to make the drink should be deducted from the coffee machine resources.

#TODO 22: b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”.
# If latte was their choice of drink.
