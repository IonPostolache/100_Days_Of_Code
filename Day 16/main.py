from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

turning_off_message = "off"
report_message = "report"

menu = Menu()
available_menu_items = menu.get_items()
drinks = available_menu_items.split("/")[0:-1]
coffe_maker = CoffeeMaker()
money_machine = MoneyMachine()


def users_prompt():
    users_response = input(f"What would you like? ({available_menu_items}):")
    return users_response


def main_function():
    response = users_prompt()
    while response != turning_off_message:
        if response == report_message:
            coffe_maker.report()
            money_machine.report()
        elif response in drinks:
            drink = menu.find_drink(response)
            if coffe_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffe_maker.make_coffee(drink)

        response = users_prompt()
    print("Turning Off the Coffee Machine...")


main_function()
