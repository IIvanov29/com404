print("Welcome to the Planet of the Apes...")

#Declaring variables for the number of times the loop will be executed and for storing the totals for humans and apes
MAX_ITERATIONS = 7
START_VALUE = 1
STEP_VALUE = 1

humans = 0
apes = 0

#Starting the loop, which will be executed the amount of times, stored in the "loop_variable"
for repetitions in range(START_VALUE,MAX_ITERATIONS,STEP_VALUE):
    #Taking the users input
    print("...be ye human or be ye ape?")
    human_or_ape = input().lower()

    #Making the decision, based on the users input
    if human_or_ape == "human":
        print("I did not start this way, but I will finish it")
        human += 1
    elif human_or_ape == "ape":
        print("Apes together strong!")
    else:
        print("This is not your fight.")

#Printing the total number of humans and the total number of apes encountered
print("Total humans encountered: " + str(humans))
print("Total apes encountered: " + str(apes))