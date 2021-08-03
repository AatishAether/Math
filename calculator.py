while(1):
	print("Press 1 to Print Author Info\nPress 2 to add\nPress 3 to subtract\nPress 4 for Factorial Math\nPress 5 for Divisbility Calculator\nPress 0 to quit\n")
	userInput = input("")
	if userInput == "1":
		print("Alex Theroux\nComputer Engineer\nFlow Architect\n")
		
	elif userInput == "2":
		num1 = float(input("Please enter a number\n"))
		num2 = float(input("Please enter another number\n"))
		result = str(num1 + num2)
		print(str(num1)  + "+" + str(num2) + "=" + result)
		
	elif userInput == "3":
		num1 = float(input("Please enter a number\n"))
		num2 = float(input("Please enter another number\n"))
		result = num1 - num2
		print(str(num1)  + " - " + str(num2) + " = " + str(result))
		
	elif userInput == "4":
                num1 = int(input("Please enter a whole number\n"))
                for nums in range(0,num1):
                        sum=nums*(nums+1)+sum
                        print(sum)
                        print(num1 + "! is: " + sum)
	elif userInput == "0":
		break;
	else:
		print("Invalid command\n")
