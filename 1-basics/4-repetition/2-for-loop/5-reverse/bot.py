#Program, which reverses a given phrase

print("What phrase do you see?")
phrase= input()

print("Reversing...")
print("The phrase is... ", end="")

for count in range (len(phrase),0,-1):
    print(phrase[count-1 ], end="")

print("")

