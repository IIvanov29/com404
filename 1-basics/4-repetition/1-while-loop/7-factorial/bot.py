#A program to calculate factorial of a number, input by the user

print("Please enter a number...")
number = int(input())

#Declaring variables.
loop_variable = number
i=0
factorial = 1

#Calculating the factorial of the number, given by the user
while(i<loop_variable):
    i += 1
    factorial = factorial * number
    number -= 1

print("The factorial is... " + str(factorial))