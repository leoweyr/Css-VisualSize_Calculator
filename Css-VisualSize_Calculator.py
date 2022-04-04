import time
import os

class ViewportSize:
    def __init__(self,vwMax,vhMax):
        self.VwMax = float(vwMax)
        self.VhMax = float(vhMax)
    def FixedToViewport_width(self,width):
        viewportWidth = float(width) / self.VwMax
        viewportWidth = str(viewportWidth)
        viewportWidth_list = viewportWidth.split('.')
        viewportWidth_backup = ""
        digit = 0
        for number in viewportWidth_list[1]:
            if (len(viewportWidth_list[1]) == 1):
                number += "0"
            if (len(viewportWidth_list[1]) > 4):
                if (int(viewportWidth_list[1][4]) > 6 and digit == 3):
                    number = str(int(number) + 1)
            viewportWidth_backup += number
            if (digit == 1):
                viewportWidth_backup += "."
            if(digit == 3):
                break
            digit += 1
        return viewportWidth_backup
    def FixedToViewport_height(self,height):
        viewportHeight = float(height) / self.VhMax
        viewportHeight = str(viewportHeight)
        viewportHeight_list = viewportHeight.split('.')
        viewportHeight_backup = ""
        digit = 0
        for number in viewportHeight_list[1]:
            if(len(viewportHeight_list[1]) == 1):
                number += "0"
            if(len(viewportHeight_list[1]) > 4):
                if (int(viewportHeight_list[1][4]) > 6 and digit == 3):
                    number = str(int(number) + 1)
            viewportHeight_backup += number
            if(digit == 1):
                viewportHeight_backup += "."
            if(digit == 3):
                break
            digit += 1
        return viewportHeight_backup

def Speaker(sentence,pause=1):
    print(sentence)
    time.sleep(pause)

def LogoPrinter():
    print("_________                 ____   ____.__                    .__    _________.__                _________        .__               .__          __                ")
    print("\_   ___ \  ______ ______ \   \ /   /|__| ________ _______  |  |  /   _____/|__|_______ ____   \_   ___ \_____  |  |   ____  __ __|  | _____ _/  |_  ___________ ")
    print("/    \  \/ /  ___//  ___/  \   Y   / |  |/  ___/  |  \__  \ |  |  \_____  \ |  \___   // __ \  /    \  \/\__  \ |  | _/ ___\|  |  \  | \__  \\   __\/  _ \_  __ ")
    print("\     \____\___ \ \___ \    \     /  |  |\___ \|  |  // __ \|  |__/        \|  |/    /\  ___/  \     \____/ __ \|  |_\  \___|  |  /  |__/ __ \|  | (  <_> )  | \/")
    print(" \______  /____  >____  >    \___/   |__/____  >____/(____  /____/_______  /|__/_____ \\___  >  \______  (____  /____/\___  >____/|____(____  /__|  \____/|__|  ")
    print("       \/     \/     \/                     \/           \/             \/          \/    \/          \/     \/          \/                \/                   ")

def Helper():
    Speaker("1. Firstly, you must set the max values of viewport width and viewport height by cmd:")
    Speaker("   set <maxValue:fixedWidth> <maxValue:fixedHeight>")
    Speaker("2. And then, you will enter the workspace, calculate and get the result by cmd:")
    Speaker("   w<value:fixedWidth> - FixedWidth to viewportWidth")
    Speaker("   h<value:fixedHeight> - FixedHeight to viewportHeight")
    Speaker("3. Also ,you can back to the first step by cmd:")
    Speaker("   r or return")
    Speaker("4. Exit the software by cmd:")
    Speaker("   x or exit")
    Speaker("Attention!!! Don't input the value with unit.")
    Speaker("\nNext, an example is used to demonstrate the animation to show the process of a solution:",2)
    Speaker("You: Input << set 1440 1024")
    Speaker("Output >> You have entered the workspace, please begin your calculating work.")
    Speaker("You: Input << w144")
    Speaker("Output >> 10vw")
    Speaker("You: Input << h102.4")
    Speaker("Output >> 10vh")
    Speaker("You can copy the result to somewhere you need.")
    Speaker("You: Input << return")
    Speaker("Output >> You have came out the workspace, please reset the max values of viewport width and viewport height.")
    Speaker("You: Input << 428 926")
    Speaker("...")
    Speaker("Understand? So, let you start the work.")

def main():
    LogoPrinter()
    time.sleep(0.5)
    Speaker("This is a light tool for convert fixed size to viewport size conveniently in web pages design of Css.",0.5)
    Speaker("Copyright (C) 2022 leoweyr",0.5)
    Speaker("Using the software for the first time?Get help by cmd: help or ?",0.5)
    workspace = 0
    while True:
        argv = input("Css ViewportSize Calculator>")
        if(argv == "help" or argv == "?"):
            Helper()
        elif(argv[0:3] == "set"):
            argv_list = argv.split(" ")
            viewportSize = ViewportSize(argv_list[1],argv_list[2])
            workspace = 1
            Speaker("You have entered the workspace, please begin your calculating work.")
        elif(argv == "x" or argv == "exit"):
            os._exit(0)
        else:
            Speaker("Need help?Get help by cmd: help or ?",0.5)
        if (workspace == 1):
            while True:
                argv = input("Workspace fixedMax[Width:" + str(viewportSize.VwMax) + "|Height:" + str(viewportSize.VhMax) + "]>")
                if(argv[0] == "w"):
                    if(float(argv[1:]) > viewportSize.VwMax):
                        Speaker("Oops! The value have been larger than the max of fixed width.")
                    else:
                        print(viewportSize.FixedToViewport_width(argv[1:]) + "vw")
                elif(argv[0] == "h"):
                    if (float(argv[1:]) > viewportSize.VhMax):
                        Speaker("Oops! The value have been larger than the max of fixed width.")
                    else:
                        print(viewportSize.FixedToViewport_height(argv[1:]) + "vh")
                elif(argv == "r" or argv == "return"):
                    print("You have came out the workspace, please reset the max values of viewport width and viewport height.")
                    return False
                elif (argv == "x" or argv == "exit"):
                    os._exit(0)
                elif(argv == "help" or argv == "?"):
                    Helper()
                else:
                    Speaker("Need help?Get help by cmd: help or ?", 0.5)

if (__name__ == '__main__'):
    main()