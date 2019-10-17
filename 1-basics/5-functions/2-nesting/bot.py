#Nesting in a function

def identify():
    print("What lies before us?")
    danger = input()
    if (danger == "a large boulder"):
        print("It's time to run!")
    else:
        print("We will be fine")

identify()