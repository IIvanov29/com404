#Returning Values

def sum_weights(weight_beep, weight_bop):
    print("The weight of the two robots is: ",weight_beep + weight_bop)

def calc_avg_weight(weight_beep, weight_bop):
    print("The average weight of the two robots is: ", (weight_beep + weight_bop)/2)

def run():
    print("How much does Beep weigh?")
    weight_beep = int(input())
    print("How much does Bop weigh?")
    weight_bop = int(input())

    print("What would you like to calculate (sum or average)?")
    decision = input()

    if (decision == "sum"):
        sum_weights(weight_beep,weight_bop)
    elif(decision == "average"):
        calc_avg_weight(weight_beep,weight_bop)

#Running the program
run()
