#Show Beeps image and health status below.
#Take Beeps number of lives
print("Please enter the number of lives:")
lives = input()

#Take beeps energy level
print("Please enter the energy level:")
energy = input()

#Take Beeps shield level
print("Please enter the shield level:")
shield = input()

#printing Beeps image
print(" ######")
print("# #  # #")
print("#      #")
print("# #### #")
print(" ###### ")
print("   #    ")
print("   #    ")
print("#########")
print("#       #")
print("#  ###  #")
print("#  # #  #")
print("#  ###  #")
print("#  # #  #")
print("#  ###  #")
print("#       #")
print("#########")
print("##     ##")
print("##     ##\n\n")

#Printing health status
print("Health is set as follows:")
print("Number of Lives: " + "♥" * int(lives))
print("Energy level: " + "♦" * int(energy))
print("Shield Level: " + "♦" * int(shield))