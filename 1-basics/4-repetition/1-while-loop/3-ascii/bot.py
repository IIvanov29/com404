#Ascii counting bot

#Taking user input
print("How many bars should be charged?")
number_of_bars = int(input())
i = 0

#Printing the phrase "Charging: with n bars next to it" (Where n is the number of times the loop has occured.)
while(i<number_of_bars):
    i += 1
    print("Charging:" + " █"*i)

print("The battery is fully charged.")