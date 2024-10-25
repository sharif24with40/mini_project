from coffee_data import MENU, resources

profit = 0

def is_resource_sufficient(order_ingredients):
    """Check if there are enough resources to make the drink."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True

def is_transaction_successful(money_received, drink_cost):
    """Process the payment and check if it's sufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False

def process_coin():
    """Calculate the total amount of money inserted."""
    try:
        print("Please insert the coins.")
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickels = int(input("How many nickels?: "))
        pennies = int(input("How many pennies?: "))

        total = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
        return total

    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return 0  # Return 0 to indicate no valid input was received

def make_coffee(order_name, ingredients):
    """Deduct the required ingredients from the resources."""
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {order_name} ☕️. Enjoy!")

is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    elif choice in MENU:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coin()
            if payment > 0:  # Check if valid payment was received
                if is_transaction_successful(payment, drink["cost"]):
                    make_coffee(choice, drink["ingredients"])
    else:
        print("Invalid selection. Please choose from the menu.")
