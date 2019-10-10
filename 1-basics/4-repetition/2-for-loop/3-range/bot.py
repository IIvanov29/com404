#Using range with a for loop

print("What level of brightness is required?")
brightness_level = int(input())

print("Adjusting brightness...")
for count in range (2,(brightness_level+2),2):
    print("Beep's brightness level:" + "*" * count)

print("Adjustments complete!")
