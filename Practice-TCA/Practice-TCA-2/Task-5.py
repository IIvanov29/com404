#Nesting

print("Your health is 100%. Escape is in progress...")

#Declaring variables, for the number of repetitions the loop will do and the health of the user
health = 100
loop_variable = 5

#Starting the loop, repeating it 5 times, with different options nested inside.
for repetition in range(0,loop_variable,1):
    print("Oh dear, who is that?")
    who_is_that = input().lower()

    if who_is_that == "smiler's bot":
        print("Time to jam out of here.")
        health -= 20
    elif who_is_that == "hacker":
        print("Yay! Better follow this one!")
        health += 20
    else:
        print("Phew, just another emoji")

#Data validation (Health can't be more than a 100)
if health > 100:
    health = 100

#Printing finishing line of the program.
print("Escaped! Health is " + str(health) + "%.")