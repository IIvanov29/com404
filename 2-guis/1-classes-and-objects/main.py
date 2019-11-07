from Bot import Bot
from SuperBot import SuperBot
from FlyingBot import FlyingBot

print("Please enter the bot's name")
bots_name = input()
print("Please enter the bot's age")
bots_age = int(input())
print("Please enter the bot's energy level")
bots_energy_level = int(input())
print("Please enter the bots shield level")
bots_shield_level = int(input())

New_Bot = Bot(bots_name,bots_age,bots_energy_level,bots_shield_level)
New_Super_Bot = SuperBot()
New_Flying_Bot = FlyingBot()

#Displaying methods
New_Bot.display_name()
New_Bot.display_age()
New_Bot.dispaly_energy()
New_Bot.display_shield()
New_Bot.display_summary()

#Returning methods
New_Bot.get_age()
New_Bot.get_name()
New_Bot.get_energy()
New_Bot.get_shield()
New_Flying_Bot.get_hover_distane()
New_Super_Bot.get_super_power_level()

#Incrementing and Decrementing Methods
New_Bot.decrement_energy(2)
New_Bot.decrement_shield(2)
New_Bot.increment_energy(3)
New_Bot.increment_shield(3)
New_Bot.increment_age()

#Setting values methods

New_Bot.set_name("Boop")
New_Super_Bot.set_super_power_level(3)
New_Flying_Bot.set_hover_distance(4)