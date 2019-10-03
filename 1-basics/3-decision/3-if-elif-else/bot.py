#Helping Beep learn to paint
#The user input (up,down,left or right) leads the direction of Beeps brush

print("Towards which direction should i paint(up, down, left or right)?")
direction = input()

if(direction == "up"):
    print("I am painting in the upward direction!")
elif(direction == "down"):
    print("I am painting in the downward direction!")
elif(direction == "left"):
    print("I am painting in the left direction!")
elif(direction == "right"):
    print("I am painting in the right direction!")
else:
    print("Please enter a valid direction")
