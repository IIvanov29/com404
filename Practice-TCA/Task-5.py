#Using Nesting

#Declaring variables
dead_ends = 0
num_of_mummies = 0

print("Escaping the tomb...")

#making a variable, which will be used by the while loop
loop_variable = 4

#Start of the loop
while loop_variable > 0:

    loop_variable -= 1

    #Taking the user's input
    print("")
    print("What lies before me?")
    seen_by_user = input()

    #Using if statements, according to the user's input
    if seen_by_user == "a dead end":
        print("Time to turn back.")
        dead_ends += 1
    elif seen_by_user == "a mummy":
        print("Better find another way")
        num_of_mummies += 1
    else:
        print("Let's move around it.\n")

print("Encountered " + str(dead_ends) + " dead ends and " + str(num_of_mummies) + " mummies.")