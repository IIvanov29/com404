#Reversing a string by using membership operators

print("What phrase do you see?")
user_word = input()

reversedstring = ""

print("Reversing...")

for letter in user_word:

    reversedstring = letter + reversedstring

print("The phrase is: " + reversedstring)

