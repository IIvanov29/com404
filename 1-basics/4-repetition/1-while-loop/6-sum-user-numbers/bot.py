#Program to sum numbers, given by the user

print("How many numbers should I sum up?")
number_of_numbers = int(input())

i = 0
Total = 0
while(i<number_of_numbers):
    i += 1
    print("Please enter number " + str(i) +" of " +str(number_of_numbers)+ ":")
    number = int(input())

    Total += number

print("The answer is: " + str(Total) +".")