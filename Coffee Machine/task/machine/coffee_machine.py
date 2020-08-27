print("""
Starting to make a coffee
Grinding coffee beans
Boiling water
Mixing boiled water with crushed coffee beans
Pouring coffee into the cup
Pouring some milk into the cup
Coffee is ready!
""")

coffee_required = int(input("Write how many cups of coffee you will need:"))
print("""
For {} cups of coffee you will need:
{} ml of water
{} ml of milk
{} g of coffee beans""".format(coffee_required, coffee_required*200, coffee_required*50, coffee_required*15))
