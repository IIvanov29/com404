#Importing everythin from the "functions.py" module
from functions import *

#Taking the word, which will be manipulated and displaying the options, from which the user has to choose
print("Please enter the word, you wish to manipulate.")
word = input()

print("Please select one of the following options")
print(""" 1 - Display the word with a line under it
2- Display the word with a line above it
3- Display the word with a lines both above and below it
4- Display the word in a grid""")

#Taking the user's option
option = input()

#Calling a function, from the functions module, chosen by the user
if option == "1":
    line_below(word)
elif option == "2":
    line_above(word)
elif option == "3":
    both_lines(word)
elif option == "4":
    display_grid(word)
else:
    print("Invalid option.Please try Again.")