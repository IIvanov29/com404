#Ascii counting bot

print("How many bars should be charged?")
number_of_bars = int(input())
i = 0

while(i<number_of_bars):
    i += 1
    print("Charging:" + " █"*i)

print("The battery is fully charged.")