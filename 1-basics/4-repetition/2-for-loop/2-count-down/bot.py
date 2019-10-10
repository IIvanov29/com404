#Program to count numbers down

print("How far are we from the cave? (In steps)")
number_of_steps = int(input())

#Declaring a variable, which will be used for the "for" loop, as the original input variable will be altered in the loop.
loop_variable = number_of_steps

for count in range(0, loop_variable):
    print("\n" + str(number_of_steps) + " steps remaining")
    number_of_steps -= 1

print("\nWe've reached the cave!")