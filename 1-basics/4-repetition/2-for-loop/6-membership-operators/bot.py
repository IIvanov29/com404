#Reversing a string by using membership operators

print("What phrase do you see?")
user_word = input()

reversedstring = ""

print("Reversing...")

for i in user_word:

    reversedstring = i + reversedstring

print("The phrase is: " + reversedstring)

