##7/21/19
##FizzBuzz

####CHALLENGE:
##Write a program that counts from 1 to ?(100)
##For every multiple of 3, write Fizz instead of the number
##For every multiple of 5, write Buzz instead of the number
##For multiples of 3 and 5, write FizzBuzz instead of the number



##Define Fn's
def fizz(num):
    fizzNum = 3
    if(num%fizzNum == 0):        
        return True
    else:
        return False

def buzz(num):
    buzzNum = 5
    if(num%buzzNum == 0):
        return True
    else:
        return False

##Declare global variables
maxCount = 100

def main():
    for i in range(1,maxCount+1):
        checkFizz = fizz(i)
        checkBuzz = buzz(i)
        if(checkFizz):            
            if(checkBuzz):
                print("FizzBuzz")
                continue
            print("Fizz")        
        elif(checkBuzz):
            print("Buzz")
        else:
            print(i)

main()
