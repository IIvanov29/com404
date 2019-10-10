#Counting program

#Taking user input
print("How many live cables should i avoid?")
number_of_cables = int(input())
i = 0

#printing the phrase "Avoiding Done "n" live cables avoided" (Where n is the number of times the while loop is went through) the amount of times set by the user input
while(i<number_of_cables):
    i += 1
    print("Avoiding...Done! " + str(i) + " live cables avoided.")

print("All live cables have been avoided.")