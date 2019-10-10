#Program, which displays a grid of ascii emojis

print("How many rows should I have?")
rows = int(input())

print("How many colums should I have?")
columns = int(input())

print("Here I go:")

for count in range (0,rows,1):
    for count in range (0,columns,1):
        print(":)",end="")
    print()


print("Done!")