#This program will help Beep find his battery
def Search():
    print("Where should i look? (bedroom,bathroom or the lab)")
    room = input()

    if(room == "bedroom"):
        print("Where in the bedroom should I look?")
        bedroomlk = input()
        if(bedroomlk == "under the bed"):
            print("Found some shoes but no battery.")
            Search()
        else:
            print("Found some mess but no battery")
            Search()
    if(room == "bathroom"):
        print("Where in the bathroom should i look?")
        bathroomlk = input()
        if(bathroomlk == "in the bathub"):
            print("Found a rubber duck but no battery")
            Search()
        else:
            print("It is wet but i found no battery.")
            Search()
    if(room == "the lab"):
        print("Where in the lab should i look?")
        lablk = input()
        if(lablk == "on the table"):
            print("Yes ! I found my battery!")
            quit()
        else:
            print("Found some tools but no battery.")
            Search()
    if(room != "bedroom") or (room != "bathroom") or (room != "the lab"):
        print("I do not know where that is but I will keep looking")
Search()