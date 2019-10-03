#Helping beep solve complex programs
#The program will get a whole number from input and output if the number is odd or even

print ("Please enter a whole number")
number = input("here: ")

if(int(number) % 2 == 1):
    print("The number " +number+ " is an odd number")
elif(int(number) % 2 == 0):
    print("The number " +number + " is an even number")
else:
    print("Please enter a valid number")
