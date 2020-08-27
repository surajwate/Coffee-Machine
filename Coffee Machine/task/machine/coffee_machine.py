machine_content = {"water": 400, "milk": 540, "beans": 120, "cups": 9, "money": 550}


def status_display(content):
    print("""
The coffee machine has:
{} of water
{} of milk
{} of coffee beans
{} of disposable cups
{} of money\n""".format(*list(content.values())))


def refill():
    refilled = {"water": int(input("Write how many ml of water do you want to add:")),
                "milk": int(input("Write how many ml of milk do you want to add:")),
                "beans": int(input("Write how many grams of coffee beans do you want to add:")),
                "cups": int(input("Write how many disposable cups of coffee do you want to add:"))}
    return refilled


def update(content, updated_content) -> dict:
    for keys in updated_content:
        content[keys] = content[keys] + updated_content[keys]
    return content


def coffee_selection(ans: str) -> dict:
    espresso = {"water": -250, "beans": -16, "cups": -1, "money": 4}
    latte = {"water": -350, "milk": -75, "beans": -20, "cups": -1, "money": 7}
    cappuccino = {"water": -200, "milk": -100, "beans": -12, "cups": -1, "money": 6}
    if ans == "1":
        return espresso
    elif ans == "2":
        return latte
    elif ans == "3":
        return cappuccino


status_display(machine_content)
action = input("Write action (buy, fill, take):")

if action == "buy":
    answer = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
    coffee_selected = coffee_selection(answer)
    machine_content = update(machine_content, coffee_selected)
elif action == "fill":
    refill_content = refill()
    machine_content = update(machine_content, refill_content)
elif action == "take":
    print("I gave you ${}".format(machine_content["money"]))
    machine_content = update(machine_content, {"money": -machine_content["money"]})

status_display(machine_content)
