#This is a review for decisions lesson
def ConfigMaker():

    print("Hello, I am Beep. Today I will help you build a system configuration.")

    def Usage():
        print("Will you be using your PC for gaming or browsing the internet?")
        use = input()

        if(use == "gaming"):
            print("We will need a quite powerful configuration")
            print("Are you going to play games, with beautiful, high-end graphics, or some less demanding games?(graphics/less demanding)")

            global pc
            pc = "gaming"
            game = input()

            if(game == "graphics"):
                print("We will need a quite powerful graphics card!")

            else:
                print("We will save money from the graphics card and invest in the other parts.")

        elif(use=="browsing"):
            print("We will need a less powerful configuration and will save money. Yay!")

            pc = "browsing"

        else:
            print("Please enter a valid usage of your future configuration")
            Usage()
        MonitorSelection()
    def MonitorSelection():
        print("Let's decide what monitor to get for you.")
        print("Would you like a high-end, high quality picture monitor, or would you like a cheaper one to save money? (high-end or high-quality /cheap)")
        monitor = input()
        global endmonitor
        if(monitor == "high-end") or (monitor== "high-quality"):
            print("So you like your games and videos in high quality, that's great!")

            endmonitor = "high-end"

        elif(monitor == "cheap"):
            print("It is good that you want to save money!")

            endmonitor = "low-end"

        else:
            print("Please enter a valid monitor type!")
            MonitorSelection()
        PrintResult()
    def PrintResult():

        if(pc == "gaming") and (endmonitor == "high-end"):
            print("You're getting a really powerful high-end setup, congratulations!")

        elif(pc == "gaming") and (endmonitor == "low-end"):
            print("You're getting quite a powerful pc, and you can always upgrade your monitor later, congratulations !")

        elif(pc == "browsing"):
            print("Congratulations on your new system, you can now browse through the internet, watch your favourite cat videos and enjoy your movies.")

    Usage()
ConfigMaker()