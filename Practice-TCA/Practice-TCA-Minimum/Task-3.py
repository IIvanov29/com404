#Loops

print("How many miles must I travel before I reach the secret base?")
miles_left = int(input())

print("I will count the miles...")

loop_variable = miles_left

for miles in range (0,miles_left, 1):

    print("I have " + str(loop_variable) + " miles to go before I reach the base.")
    loop_variable -= 1

print("I have arrived at the secret headquarters of MIB!")
print("It is time to sneak in")