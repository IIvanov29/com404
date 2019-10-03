#We will help beep to pick an adventure

print("What type of adventure should I have?")
adventure_type = input()

if(adventure_type == "short") or (adventure_type == "scary"):
    print("Entering the dark forest !")
elif(adventure_type == "safe") or (adventure_type == "long"):
    print("Taking the safe route!")
else:
    print("Im not sure which route to take.")

