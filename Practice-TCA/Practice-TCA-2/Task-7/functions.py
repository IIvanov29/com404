#Creating a python module, which executes the functions, called by "main.py"
def line_below(word):
    print(word)
    print("*" * len(word))

def line_above(word):
    print("*" * len(word))
    print(word)

def both_lines(word):
    print("*" * len(word))
    print(word)
    print("*" * len(word))

def display_grid(word):
    print("How big would you like you grid to be (maximum of 3)?")
    grid_size = int(input())

    if grid_size > 3:
        grid_size = 3

    for grid in range(0,grid_size,1):
        print(("*" * len(word)) * grid_size)
        print((word + "|") * grid_size)
        print(("*" * len(word)) * grid_size)