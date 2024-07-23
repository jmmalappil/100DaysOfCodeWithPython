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


# TODO 2: Print report of resources available:
def print_resources(res, prof):
    print(f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"coffee: {resources['coffee']}")
    print(f"Money: ${profit}")


# TODO 3: Check if resources are sufficient:
def check_resources(inp):
    is_sufficient = False
    if inp == 'espresso':
        if resources['water'] >= MENU[inp]['ingredients']['water']:
            if resources['coffee'] >= MENU[inp]['ingredients']['coffee']:
                is_sufficient = True
                resources['coffee'] -= MENU[inp]['ingredients']['coffee']
                resources['water'] -= MENU[inp]['ingredients']['water']
            else:
                print("Sorry there is not enough coffee")
        else:
            print("Sorry there is not enough water")
    else:
        if resources['water'] >= MENU[inp]['ingredients']['water']:
            if resources['coffee'] >= MENU[inp]['ingredients']['coffee']:
                if resources['milk'] >= MENU[inp]['ingredients']['milk']:
                    is_sufficient = True
                    resources['coffee'] -= MENU[inp]['ingredients']['coffee']
                    resources['water'] -= MENU[inp]['ingredients']['water']
                    resources['milk'] -= MENU[inp]['ingredients']['milk']
                else:
                    print("Sorry there is not enough milk")
            else:
                print("Sorry there is not enough coffee")
        else:
            print("Sorry there is not enough water")
    return is_sufficient


# TODO 4: Process coins

def process_coins(inp):
    balance = 0
    is_successful = False
    print("Please insert coins.")
    quarters = int(input("How many quarters?:"))
    dimes = int(input("How many dimes?:"))
    nickles = int(input("How many quarters?:"))
    pennies = int(input("How many pennies?:"))
    total = round((quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01),2)
    if total > MENU[inp]["cost"]:
        print(total)
        is_successful = True
    return is_successful, total


# TODO 1: Prompt user by asking “ What would you like? (espresso/latte/cappuccino):
profit = 0

is_continue = True

while is_continue:

    choice = input("What would you like? (espresso/latte/cappuccino):")

    if choice == 'report':
        print_resources(resources, profit)
    elif choice == 'espresso':
        res_available = check_resources(choice)
        if res_available:
            is_success, tot = process_coins(choice)
            if is_success:
                profit = profit + MENU['espresso']['cost']
                change = tot - MENU['espresso']['cost']
                print(f"Here is ${change} in change")
                print("Here is your 'espresso' ☕ Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded")

    elif choice == 'latte':
        res_available = check_resources(choice)
        if res_available:
            is_success, tot = process_coins(choice)
            if is_success:
                profit = profit + MENU['latte']['cost']
                change = tot - MENU['latte']['cost']
                print(f"Here is ${change} in change")
                print("Here is your 'latte' ☕ Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded")
    elif choice == 'cappuccino':
        res_available = check_resources(choice)
        if res_available:
            is_success, tot = process_coins(choice)
            if is_success:
                profit = profit + MENU['cappuccino']['cost']
                change = tot - MENU['cappuccino']['cost']
                print(f"Here is ${change} in change")
                print("Here is your 'cappuccino' ☕ Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded")
    elif choice == 'off':
        print("Bye, have a good day")
        break
    else:
        print("You have entered a wrong choice")
