#We will help Beep classify his books

print("What type of cover does the book have? (soft or hard)")
cover_type = input()

if(cover_type == "soft"):
    print("Is the book perfect-bound?")
    pbound = input()
    if(pbound == "yes"):
        print("soft cover, perfect bound books are very popular!")
    else:
        print("Soft cfovers with couils or stitches are great for short books.")
else:
    print("Books with hard covers can be more expensive!")