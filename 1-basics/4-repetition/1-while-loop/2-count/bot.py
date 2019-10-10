#Counting program

print("How many live cables should i avoid?")
number_of_cables = int(input())
i = 0

while(i<number_of_cables):
    i += 1
    print("Avoiding...Done! " + str(i) + " live cables avoided.")

print("All live cables have been avoided.")