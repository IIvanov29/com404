#Loop

print("How many zones must I cross?")
zones_to_cross = int(input())

print("Crossing zones...")

loop_variable = zones_to_cross
for zones in range(0,zones_to_cross,1):

    print("...crossed zone " + str(loop_variable))
    loop_variable -= 1

print("Crossed all zones. Jumanji!")