#A program, which will help Siren, with creating a beatiful banner

def Under_lining(message):
    print("Halloween")
    print("-" * len(message))
    print(message)

def Over_lining(message):
    print(message)
    print("-" * len(message))
    print("Halloween")

def Display_both(message):
    print(message)
    print("-" * len(message))
    print("Halloween")
    print("-" * len(message))
    print(message)

def Display_grid(message):

    message_lenght = len(message)

    if message_lenght >= 5:
        message_lenght = 5

    for count in range (0,message_lenght,1):
        print("Halloween|" * message_lenght)



def TakeInput(message):

    if message == "":
        print("Enter the message, which you would like to use for the banner")
        message = input()
    print("Please select an option for your banner!")
    print("""1 - Display your banned with a line under your message
2 - Display your banner with a line over your message
3 - Display your banner with both underline and an overline
4 - Display a grid with the word Halloween""")
    user_option = input()

    if user_option == "1":
        Under_lining(message)
    elif user_option == "2":
        Over_lining(message)
    elif user_option == "3":
        Display_both(message)
    elif user_option == "4":
        Display_grid(message)
    else:
        print("Please enter a valid option")
        TakeInput("")


TakeInput("")

