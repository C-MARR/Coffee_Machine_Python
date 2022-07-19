import drink

required_water = 200
required_milk = 50
required_beans = 15
water_ml = 400
milk_ml = 540
bean_grams = 120
cups = 9
money = 550


possible_with_water = water_ml // required_water
possible_with_milk = milk_ml // required_milk
possible_with_beans = bean_grams // required_beans

if cups <= possible_with_water and cups <= possible_with_milk and cups <= possible_with_beans:
    response = "Yes, I can make that amount of coffee"
    possible_cups = min(possible_with_water, possible_with_milk, possible_with_beans)
    if possible_cups > cups:
        response += f" (and even {possible_cups - cups} more than that)"
    print(response)
else:
    print(f"No, I can make only {min(possible_with_water, possible_with_milk, possible_with_beans)} cups of coffee")


def display_machine_supplies():
    print("The coffee machine has:\n"
          + f"#{water_ml} ml of water\n"
          + f"#{milk_ml} ml of milk\n"
          + f"#{bean_grams}g of coffee beans\n"
          + f"#{cups} disposable cups\n"
          + f"$#{money} of money\n")


def add_supplies():
    global water_ml
    global milk_ml
    global bean_grams
    global cups
    print("Write how many ml of water you want to add:")
    water_ml += int(input())
    print("Write how many ml of milk you want to add:")
    milk_ml += int(input())
    print("Write how many grams of coffee beans you want to add:")
    bean_grams += int(input())
    print("Write how many disposable cups you want to add:")
    cups += int(input())
