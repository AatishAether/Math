import argparse

##plot the numbers
##print highest number reached
##Number < 1.000.000 w/ highest steps && number w/ highest number reached
##multiprocessing

def main():
    ap = argparse.ArgumentParser(description="Collatz conjecture: Checks that a given number collapses to zero")
    ap.add_argument('-n','--number',dest="number",required=True,help="Provide a number for the conjecture")
    args = ap.parse_args()

    val = int(args.number)
    count = 0
    print(val)
    while(val != 1):  
        ##print(val)      
        if(val % 2 !=0):
            val = val * 3 + 1
            count += 1
        elif(val % 2 == 0):
            val = val/2
            count += 1
    print("Finished!\n" + args.number + " took " + str(count) + " steps to complete")

if __name__ == '__main__':
    main()
