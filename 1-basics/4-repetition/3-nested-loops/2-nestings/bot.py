#Program, which will count the distance in dashes between two markers

print("Please enter a sequence")
sequence = input()

print("Please enter a character for the marker")
marker = input()

marker1_position = -1
marker2_position = -2

for position in range(0,len(sequence),1):

    letter = sequence[position]

    if letter == marker:
        if marker1_position<=0:
            marker1_position = position
        if marker1_position >= 0:
            marker2_position = position


distance = (marker2_position - marker1_position)-1

print("The distance is: " + str(distance))


