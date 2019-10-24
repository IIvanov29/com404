#Using a loop to repeat strings

print("How many days remain until the next full moon?")
days_left = int(input())
print("We must count the days")

loop_variable = days_left
for count in range (0,loop_variable):
    print("The full moon will be upon us in " + str(days_left) + " days")
    days_left -= 1

print("It's a full moon, the beast has been unleashed!")
print("May it have mercy on our souls")