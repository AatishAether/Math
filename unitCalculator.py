import constant
import calendar

#declare global variables & const

#define FNs
def distance():
    print("You chose english distance")
    INCH = 1
    FOOT = INCH*12
    YARD = FOOT*3
    MILE = YARD*1760
    return

def weights():
    print("You chose enlgish weights")
    OUNCE = 1
    POUND = OUNCE*16
    TON = POUND*2000
    
    return

def liquid():
    print("You chose english liquids")
    FLOUNCE = 1
    CUP = FLOUNCE*8
    PINT = CUP*2
    QUART = PINT*2
    GAL = QUART*4
    return

def time():
    YEAR = 
    #Year = 52.142857142857142857*WEEK
    


def main():
#declare variables
    menuChoice = 0

#mainLoop
    done = False
    while not done:
    #display menu
        print("Please chose an option:\n1 - Distance\n2 - Weights")
        print("3 - Liquids and Volume")
        menuChoice = int(input())
        if menuChoice == 1:
            distance()
        elif menuChoice == 2:
            weights()
        elif menuChoice == 3:
            liquid()
        else:
            print("Input not recognized!")


main()
