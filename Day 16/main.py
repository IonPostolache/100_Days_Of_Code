from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu_items = Menu()
options = menu_items.get_items()


def users_prompt():
    users_response = input(f"What would you like? ({options}):")
    return users_response


response = users_prompt()
turn_off_message = "off"
coffe = CoffeeMaker()
drinks = options.split("/")[0:-1]
print(drinks)

while response != turn_off_message:
    if response == "report":
        coffe.report()
    elif response in drinks:
        print("yes, response in drinks")

        # coffe.is_resource_sufficient(response)
        # can_make = CoffeeMaker().is_resource_sufficient(response)
        menu2 = MenuItem()
        can_make2 = menu2.ingredients
        can_make = coffe.is_resource_sufficient(response)
        if can_make:
            print("can_make = True")
    # else:
    #     print("no")
    response = users_prompt()





print("Turning Off the Coffee Machine...")
