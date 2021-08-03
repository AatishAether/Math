import csv
import math

def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier

class PrimeHandler():
    
    
###Declare Functions
    #primes = csvfile where primes are stored
    def __init__(self,primes,perRow=1000,rows=1000):
        self.primes = primes
        #primes per row = 1000!
        self.perRow = perRow
        #1000 rows = 1,000,000 primes per csv
        self.rows = rows
        
        #Load primeData into a list
        self.primeData = PrimeHandler.load_primes(self)
        if self.primeData is None:
                        #Sieve -    low,high
            PrimeHandler.sieve(self,0,self.perRow)
            self.primeData = PrimeHandler.load_primes(self)
        end = len(self.primeData[0])
        print(end)

    def load_primes(self):
        try:
            primeFile = open(self.primes)
            primeReader = csv.reader(primeFile)
            primeData = list(primeReader)
            print("Loaded Data!")
        except FileNotFoundError:
            primeData = None            
        return primeData

    #Saves new row to existing data
    def save_primes(self,primeData):
        primeFile = open(self.primes,'a',newline='')
        primeFileWriter = csv.writer(primeFile)
        primeFileWriter.writerow(primeData)
        print("New rows saved!")
        primeFile.close()
    

    #Sieve gets called when operations require higher numbers
    def sieve(self,low,high):
        print("Sieve of Eratosthenes")
        prime_list = []    
        for i in range(low,high+1):
            check_prime = PrimeHandler.checkPrime(self,i)
            if(check_prime):
                prime_list.append(i)
##        print(prime_list)
        PrimeHandler.save_primes(self,prime_list)

    def checkRow(self,maxInt):
        if(maxInt > len(self.primeData[0])):
            last = len(self.primeData[0])-1
            #Round to the nearest thousand. Should be based off of perRow instead
            nextRow = int(round_up(len(self.primeData[0])-1,-3))
            #Run sieve on next perRow numbers
            primeHandler.sieve(nextRow,self.perRow+nextRow)
            

    def checkPrime(self,n):
        #Check primes list before calculating?
        #Slows down sieve dramatically
        
        ##Checks every 6 numbers up to sqrt(n)
        ##Only need to check up to sqrt(n) b/c if it's non-prime, any factor above sqrt(n)
        ##will have correlating factor below sqrt(n)
        ##Only need to check every 6 numbers b/c mod2 and mod3.
        
        if n == 2 or n == 3: return True
        if n<2 or n%2 == 0: return False
        if n % 3 == 0: return False
        if n < 9: return True ##Fancy way of removing 5 & 7 after mod2 and mod3
        r = int(n**0.5)
        f = 5
        ##Count every 6, starting at 5 while checking 2 ahead
        while f <= r:
            if n % f == 0: return False
            if n % (f+2) == 0: return False
            f += 6
        return True

        
    
    def list_NthPrime(self,n):
        
        if (n>len(self.primeData[0])):
            print("N > primeData")
            
        return self.primeData[0][n]
        
        

    #List primes from 1 to n
    def list_primes(self,n):
        pass
        

    #Find region of primes and nth prime of region
    def primeRegion(self):        
        start = input("Start of Region: ")
        end = input("End of Region: ")
        
    #Find quad primes
    def quadPrimes(self):
        print("quadPrimes")

        
primeHandler = PrimeHandler('primeList.csv')

print(primeHandler.checkPrime(2001))

            
##if __name__ == '__main__':
##    main()
