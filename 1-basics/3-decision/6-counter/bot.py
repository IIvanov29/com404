#We will help Beep learn to count the number of even and the number of odd numbers entered by the user
#The program will take 3 numbers as input and will output the number of odd and the number of even numbers entered

print("Please enter the first whole number")
n1 = int(input())

print("Please enter the second whole number")
n2 = int(input())

print("Please enter the third whole number")
n3 = int(input())

even = 0
odd = 0

if(n1 % 2 == 0):
    even += 1
elif(n1 % 2 == 1):
    odd += 1

if(n2 % 2 == 0):
    even += 1
elif(n2 % 2 == 1):
    odd += 1

if(n3 % 2 == 0):
    even += 1
elif(n3 % 2 == 1):
    odd += 1


print("There were " + str(even) +" even and " + str(odd) + " odd numbers.")