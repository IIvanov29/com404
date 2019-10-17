#Word Manipulation

def Display_in_a_box(word):
    print("-" * len(word))
    print("|" + word + "|")
    print("-" * len(word))

    TakeOption(word)

def Display_lower_case(word):
    print(word.upper())

    TakeOption(word)

def Display_upper_case(word):
    print(word.upper())

    TakeOption(word)

def Display_Mirrored(word):
    reversedword = ""

    for letter in word:

        reversedword =  letter + reversedword

    print(word + " | " + reversedword)

    TakeOption(word)

def Repeatt(word):
    print("How many times would you like to repeat the word?")
    times = int(input())

    for count in range (0, times, 1):
        print(word)

    TakeOption(word)

def TakeOption(word):
    if word == "":
        print("Please enter the word, you would like to process:")
        word = input()

    print("Please select on of the following options:")
    print("""1) Display in a Box – display the word in an ascii art box
2) Display Lower-case – display the word in lower-case
3) Display Upper-case – display the word in upper-case
4) Display Mirrored – display the word with its mirrored word
5) Repeat – ask the user how many times to display
the word and then display the word that many times alternating between
upper-case and lower-case.)""")
    print("To exit the program enter \"Exit\"")

    option = input()
    if option == "1":
        Display_in_a_box(word)
    elif option == "2":
        Display_lower_case(word)
    elif option =="3":
        Display_upper_case(word)
    elif option == "4":
        Display_Mirrored(word)
    elif option == "5":
        Repeatt(word)
    elif option == "Exit":
        exit()
    else:
        print("Please enter a valid option !")
        TakeOption(word)

TakeOption("")

