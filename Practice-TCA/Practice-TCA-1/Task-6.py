
def is_slow_zombie(zombie_speed):
    if (zombie_speed < 5):
        return True
    elif (zombie_speed > 5):
        return False

def take_action(zombie_speed,zombies_mutation):

    zombies_speed = is_slow_zombie(zombie_speed)

    if zombies_speed == True:
        print("This " + zombies_mutation + " zombie is a slow zombie. You can run around it!")
    elif zombies_speed == False:
        print("This " + zombies_mutation + " zombie is a fast zombie. You better hide!")

def run():


    print("What is the mutation type of the zombie?")
    zombies_mutation = input()
    print("What is the speed of the zombie?")
    zombie_speed = int(input())
    print("What do you wish to do (identify or action)?")
    user_decision = input()

    is_slow_zombie(zombie_speed)

    if user_decision == "identify":
        print("A slow zombie:",is_slow_zombie(zombie_speed))

    elif user_decision == "action":
        take_action(zombie_speed,zombies_mutation)
run()

