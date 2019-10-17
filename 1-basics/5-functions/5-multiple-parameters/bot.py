#Using multiple parameteres in a function

def climb_ladder(sremaining, scrossed):
    if sremaining > scrossed:
        print("Still some way to go!")
    elif scrossed > sremaining:
        print("We are almost there!")

climb_ladder(5,2)
climb_ladder(2,5)