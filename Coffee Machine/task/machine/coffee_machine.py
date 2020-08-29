class CoffeeMachine:

    def __init__(self):
        self.machine_content = {"water": 400, "milk": 540, "beans": 120, "cups": 9, "money": 550}

    def status_display(self, content):
        print("""
    The coffee machine has:
    {} of water
    {} of milk
    {} of coffee beans
    {} of disposable cups
    ${} of money\n""".format(*list(content.values())))

    def refill(self):
        refilled = {"water": int(input("Write how many ml of water do you want to add:")),
                    "milk": int(input("Write how many ml of milk do you want to add:")),
                    "beans": int(input("Write how many grams of coffee beans do you want to add:")),
                    "cups": int(input("Write how many disposable cups of coffee do you want to add:"))}
        return refilled

    def update(self, content, updated_content, act) -> dict:
        content_before_update = content.copy()
        for keys in updated_content:
            content[keys] = content[keys] + updated_content[keys]
        if min(list(content.values())[:4]) <= 0:
            for key in content:
                if content[key] <= 0:
                    print("Sorry, not enough {}!\n".format(key))
                    return content_before_update
        if act == "buy":
            print("I have enough resources, making you a coffee!\n")
        return content

    def coffee_selection(self, ans: str) -> dict:
        espresso = {"water": -250, "beans": -16, "cups": -1, "money": 4}
        latte = {"water": -350, "milk": -75, "beans": -20, "cups": -1, "money": 7}
        cappuccino = {"water": -200, "milk": -100, "beans": -12, "cups": -1, "money": 6}
        if ans == "1":
            return espresso
        elif ans == "2":
            return latte
        elif ans == "3":
            return cappuccino


coffee = CoffeeMachine()
while True:
    action = input("Write action (buy, fill, take, remaining, exit):")
    if action == "buy":
        answer = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
        if answer == "back":
            continue
        coffee_selected = coffee.coffee_selection(answer)
        coffee.machine_content = coffee.update(coffee.machine_content, coffee_selected, action)
    elif action == "fill":
        refill_content = coffee.refill()
        coffee.machine_content = coffee.update(coffee.machine_content, refill_content, action)
    elif action == "take":
        print("I gave you ${}".format(coffee.machine_content["money"]))
        coffee.machine_content["money"] = 0
    elif action == "remaining":
        coffee.status_display(coffee.machine_content)
    elif action == "exit":
        break


