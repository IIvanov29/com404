#printing a word, character by character

print("What strange markings do you see?")
markings = input()

for count in range (0,len(markings),1):
    print("index " + str(count) + ": " +markings[count])

print("Done!")
