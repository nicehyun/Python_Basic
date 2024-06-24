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


def report_resources(current_resources):
    UNIT = {
        "water": "ml",
        "milk": "ml",
        "coffee": "g",
        "money": "$"
    }
    report = ""

    if "money" not in current_resources:
        current_resources["money"] = 0

    for key, value in current_resources.items():
        if key == "money":
            report += f"{key.title()} : {UNIT[key]}{value}"
        else:
            report += f"{key.title()} : {value}{UNIT[key]}\n"

    return report


def check_resources_sufficient(menu, current_resources):
    ingredients = MENU[menu]["ingredients"]
    for key, value in ingredients.items():
        if current_resources[key] < value:
            print(f"😅 Sorry there is not enough {key}.\n")
            return False

    return True


def insert_money():
    QUARTERS = 0.25
    DIMES = 0.10
    NICKLES = 0.05
    PENNIES = 0.01

    print("💰 insert coin🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻")
    quarters = int(input("🪙 quarters : "))
    dimes = int(input("🪙 dimes : "))
    nickles = int(input("🪙 nickles : "))
    pennies = int(input("🪙 pennies : "))
    print("🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺\n")

    total_money = QUARTERS * quarters + DIMES * dimes + NICKLES * nickles + PENNIES * pennies
    return round(total_money, 2)


def check_enough_money(menu, inserted_money):
    menu_price = MENU[menu]["cost"]
    if menu_price > inserted_money:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        if "money" not in resources:
            resources["money"] = 0

        change = round(inserted_money - menu_price, 2)
        resources["money"] += menu_price
        print(f"Here is ${change} dollars in change.")
        return True


def make_coffee(menu):
    # TODO : 7. . Make Coffee.
    ingredients = MENU[menu]["ingredients"]
    for key, value in ingredients.items():
        resources[key] -= value


def coffe_machine():
    SECRET_POWER_OFF_KEY = "off"

    selected_menu = input("☕️ What would you like? (espresso/latte/cappuccino): ")

    if selected_menu == SECRET_POWER_OFF_KEY:
        return
    elif selected_menu == "report":
        report = report_resources(resources)
        print("🧾🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻")
        print(report)
        print("🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺\n")
        return coffe_machine()

    is_check_resources_sufficient = check_resources_sufficient(menu=selected_menu, current_resources=resources)
    if not is_check_resources_sufficient:
        return coffe_machine()

    total_money = insert_money()
    is_check_enough_money = check_enough_money(selected_menu, total_money)
    if is_check_enough_money:
        make_coffee(selected_menu)
        print("☕️ Here is your latte. Enjoy!\n")

    return coffe_machine()


coffe_machine()
