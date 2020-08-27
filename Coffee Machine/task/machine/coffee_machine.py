water = int(input("Write how many ml of water the coffee machine has:"))
milk = int(input("Write how many ml of milk the coffee machine has:"))
beans = int(input("Write how many grams of coffee beans the coffee machine has:"))
coffee_require = int(input("Write how many cups of coffee you will need:"))

coffee_make = min([water//200, milk//50, beans//15])

if coffee_make == coffee_require:
    print("Yes, I can make that amount of coffee")
elif coffee_make < coffee_require:
    print("No, I can make only {} cups of coffee".format(coffee_make))
else:
    print("Yes, I can make that amount of coffee (and even {} more than that)".format(coffee_make-coffee_require))

