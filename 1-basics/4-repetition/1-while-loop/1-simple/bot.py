#Basic while loop

#Taking user input
print("How many cables should I remove?")
number_of_cables = int(input())
i = 0

#printing the phrase "Removed cable" the amount of times set by the user input
while(i < number_of_cables):
    print("Removed cable.")
    i +=1
