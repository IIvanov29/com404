#Teaching beep about comparison of numbers
#The program will take two numbers and decide, which of the two numbers is the smallest, or if they are equal

print("Please enter the first number.")
n1 = input()

print("Please enter the second number.")
n2 = input()

if(int(n1) > int(n2)):
    print("The second number is the smallest.")
elif(int(n1) < int(n2)):
    print("The first number is the smallest.")
elif(int(n1) == int(n2)):
    print("The two numbers are equal")
