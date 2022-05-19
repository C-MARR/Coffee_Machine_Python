required_water = 200
required_milk = 50
required_beans = 15

print("Write how many ml of water the coffee machine has:")
water_ml = int(input())
print("Write how many ml of milk the coffee machine has:")
milk_ml = int(input())
print("Write how many grams of coffee beans the coffee machine has:")
bean_grams = int(input())
print("Write how many cups of coffee you will need:")
cups = int(input())

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
