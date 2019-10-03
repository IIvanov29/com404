#We will help Beep deciding whether to go deeper into the forest or find a way out

print("What did I hear?")
noise = input()

print("What did I see?")
seen = input()

if(noise == "grr") and (seen=="two red eyes"):
    print("There is a scary creature. I should get out of here!")
else:
    print("I am a little scared but I will continue !")