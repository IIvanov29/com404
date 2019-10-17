#Loop with a function

def cross_bridge(distance):
    for count in range (0,distance, 1):
        print("Crossed step")
    if distance > 5:
        print("The bridge is collapsing!")
    else:
        print("we must keep going")

cross_bridge(6)
cross_bridge(3)
