#Loop

print("How many heroes must we gather?")
number_of_heroes = int(input())

print("Gathering heroes...")

for heroes in range (1,(number_of_heroes + 1),1):

    print("...found hero " + str(heroes))

print("...all the heroes have been gathered")