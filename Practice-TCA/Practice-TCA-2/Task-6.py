#Functions

def is_league_united(Hero_1,Hero_2):

    if Hero_1 == "superman" and Hero_2 == "wonder woman":
        return True
    else:
        return False



def decide_plan(Hero_1,Hero_2):

    league_is_united = is_league_united(Hero_1,Hero_2)

    if league_is_united == True:
        print("Time to save the world!")

    elif league_is_united == False:
        print("We must unite the league!")

def run():
    print("What is the name of the first Hero?")
    Hero_1 = input().lower()

    print("What is the name of the second Hero?")
    Hero_2 = input().lower()

    print("Please select an optiong (league/plan)")
    function_option = input().lower()

    if function_option == "league":
        is_league_united(Hero_1,Hero_2)
        print(is_league_united(Hero_1,Hero_2))

    elif function_option == "plan":
        decide_plan(Hero_1,Hero_2)

    else:
        print("Invalid command! Please try again.")


run()