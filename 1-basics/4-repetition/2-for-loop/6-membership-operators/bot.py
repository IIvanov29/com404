#Reversing a string by using membership operators

print("What phrase do you see?")
user_word = input()

i = 1

for [i] in user_word :
    i+=1
    reversedphrase =[i] + reversedphrase

print(reversedphrase)