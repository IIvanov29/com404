#Bmi calculator bot

#Take users name
print("What is your name human?")
name=input()

#Take users age
print("How old are you "+name+" ? (In years)")
age=input()

#Take users height
print("How tall are you, "+name+" ? (In meters)")
height=input()

#Take users weight
print("How much do you weigh, human? (In kilograms)")
weight=input()

bmi=float(weight)/float(height) ** 2

print(name+" you are "+age+" years old and your bmi is "+str(bmi)+" !" )