#Classes and Objects

class Bot:
    def __init__(self, bot_name, bot_age,bot_energy,bot_shield):
        self.__name = bot_name
        self.__age = bot_age
        self.__energy = bot_energy
        self.__shield = bot_shield

    def get_name(self):
            return self.__name

    def get_age(self):
            return int(self.__age)

    def get_energy(self):
            return int(self.__energy)

    def get_shield(self):
            return self.__shield


    def display_name(self):
        print("--" * len(self.__name))
        print("| {} |".format(self.__name))
        print("--" * len(self.__name))
        print("=========================")

    def display_age(self):
        print("   " + str(self.__age))
        print("  ---")
        print(" /   \\")
        print(" ------")
        print("/     \\")
        print("=========================")

    def dispaly_energy(self):
        print("The current energy level of the bot is: {}" .format("|-| " * int(self.__energy)))
        print("=========================")

    def display_shield(self):
        print("---------")
        print("|       |")
        print("|   {}   |".format(self.__shield))
        print("|       |")
        print("---------")
        print("=========================")

    def display_summary(self):
        print("""My name is {}.
I am {} years old.
My current Energy Level is {}.
My current Shield Level is {}.""".format(self.__name,self.__age,self.__energy,self.__shield))
        print("=========================")

    def decrement_energy(self,decremented_energy):
        self.__energy -= decremented_energy

    def decrement_shield(self,decremented_shield):
        self.__shield -= decremented_shield

    def increment_age(self):
        print("How much would you like to add to your bot's age?")
        incremented_age = int(input())
        self.__age += incremented_age

    def increment_energy(self, incremented_energy):
        self.__energy += incremented_energy

    def increment_shield(self,incremented_shield):
        self.__shield += incremented_shield

    def set_name(self, new_bot_name):
        self.__name == new_bot_name