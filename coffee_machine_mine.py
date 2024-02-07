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

profit = 0
def report():
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    print(f"Water = {water}, Milk = {milk}, Coffee = {coffee}, Profit = {profit}")

def money():
    print("Please insert coins")
    quarters = int(input("How many quarters? ")) * 0.25
    dimes = int(input("How many dimes? ")) * 0.10
    nickles = int(input("How many nickles? ")) * 0.05
    pennies = int(input("How many pennies? ")) * 0.01
    total = (quarters + dimes + nickles + pennies)
    if choice == "espresso" and total < 1.50:
        global profit
        profit -= 1.50
        resources["water"] += 50
        resources["coffee"] += 18
        print("Sorry, you do not have enough change")

    elif resources["water"] < 0 or resources["coffee"] < 0:
        print("Out of stock")
    elif choice == "espresso" and total >= 1.50:
        change = total - 1.50
        rounded_change = round(change, 2)
        print(f"You have ${rounded_change} change. ")
        print("here is your espresso. Enjoy!")

    elif choice == "latte" and total < 2.50:
        profit -= 2.5
        resources["water"] += 200
        resources["milk"] += 150
        resources["coffee"] += 24
        print("Sorry, you do not have enough change")

    elif resources["water"] < 0 or resources["coffee"] < 0 or resources["milk"] < 0:
        print("Out of stock")
    elif choice == "latte" and total >= 2.50:
        change = total - 2.50
        rounded_change = round(change, 2)
        print(f"You have ${rounded_change} change. ")
        print("here is your latte. Enjoy!")

    elif resources["water"] < 0 or resources["coffee"] < 0 or resources["milk"] < 0:
        print("Out of stock")
    elif choice == "cappuccino" and total >= 3:
        change = total - 3
        rounded_change = round(change, 2)
        print(f"You have ${rounded_change} change. ")
        print("here is your cappuccino. Enjoy!")

    elif choice == "cappuccino" and total < 3:
        profit -= 3.0
        resources["water"] += 250
        resources["milk"] += 100
        resources["coffee"] += 24
        print("Sorry, you do not have enough change")

while resources["water"] >= 0 and resources["coffee"] >= 0 and resources["milk"] >= 0:
    choice = input("What would you like to order? Espresso, Latte or Cappuccino: ").lower()
    if choice == "off":
        break
    elif choice == "report":
        report()
    elif choice == "espresso":
        money()
        resources["water"] -= 50
        resources["coffee"] -= 18
        profit += 1.50
    elif choice == "latte":
        profit += 2.5
        resources["water"] -= 200
        resources["milk"] -= 150
        resources["coffee"] -= 24
        money()
    elif choice == "cappuccino":
        profit += 3.0
        resources["water"] -= 250
        resources["milk"] -= 100
        resources["coffee"] -= 24
        money()
    else:
        print("You made the wrong selection. Please try again")