#Program, which prints a number of mountains, set by the user input

print("How many mountains should I display?")
number_of_mountains = int(input())

for count in range (number_of_mountains):
    print(" __")
    print("/  \_")
    print("/^    \\")
    print("/  ^    \_")
    print("_/ ^ ^     ^\\")
    print("/  ^     ^    \\")