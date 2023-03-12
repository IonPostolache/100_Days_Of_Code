from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

turning_off_message = "off"
report_message = "report"

menu = Menu()
available_menu_items = menu.get_items()
drinks = available_menu_items.split("/")[0:-1]
# print(drinks)

coffe_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu_item = MenuItem()


def users_prompt():
    users_response = input(f"What would you like? ({available_menu_items}):")
    return users_response


def main_function():
    response = users_prompt()
    while response != turning_off_message:
        if response == report_message:
            coffe_maker.report()
        elif response in drinks:
            # print("yes, response in drinks")
            drink = menu.find_drink(response)
            # print(f"found drink: {drink.name}")
            if coffe_maker.is_resource_sufficient(drink):
                money_machine.make_payment(menu_item.cost)

                coffe_maker.make_coffee(drink)

        response = users_prompt()
    print("Turning Off the Coffee Machine...")


main_function()

