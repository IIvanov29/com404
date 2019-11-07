#Classes and Objects

class Bot:
    def __init__(self, bot_name, bot_age,bot_energy,bot_shield):
        self.name = bot_name
        self.age = bot_age
        self.energy = bot_energy
        self.shield = bot_shield

    def display_name(self):
        print("--" * len(self.name))
        print("| {} |".format(self.name))
        print("--" * len(self.name))
        print("=========================")

    def display_age(self):
        print("   " + self.age)
        print("  ---")
        print(" /   \\")
        print(" ------")
        print("/     \\")
        print("=========================")

    def dispaly_energy(self):
        print("The current energy level of the bot is: {}" .format("|-| " * int(self.energy)))
        print("=========================")

    def display_shield(self):
        print("---------")
        print("|       |")
        print("|   {}   |".format(self.shield))
        print("|       |")
        print("---------")
        print("=========================")

    def display_summary(self):
        print("""My name is {}.
I am {} years old.
My current Energy Level is {}.
My current Shield Level is {}.""".format(self.name,self.age,self.energy,self.shield))
        print("=========================")



print("Please enter the bot's name")
bots_name = input()
print("Please enter the bot's age")
bots_age = input()
print("Please enter the bot's energy level")
bots_energy_level = input()
print("Please enter the bots shield level")
bots_shield_level = input()

New_Bot = Bot(bots_name,bots_age,bots_energy_level,bots_shield_level)

New_Bot.display_name()
New_Bot.display_age()
New_Bot.dispaly_energy()
New_Bot.display_shield()
New_Bot.display_summary()