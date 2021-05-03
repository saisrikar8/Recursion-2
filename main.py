'''
04/29/2021
Recursion

'''

#Factorial
# 5! = 5 * 4 * 3* 2 * 1 = 120

#for loop
def forFact():
	integer = int(input("Enter a positive int:\n"))
	factorial = 1
	for i in range(1,integer + 1):
		factorial *= i
	print("The factorial of " + str(integer) + " is " + str(factorial))

#Recursion
def recFact():
	integer = int(input("Enter a positive int:\n"))
	def fact(x):
		if (x == 1):
			return 1
		else:
			return x * fact(x-1)
	print("The factorial of " + str(integer) + " is " + str(fact(int(input("Enter a positive int:\n")))))



#Fibonacci sequence
# F(0) = 0, F(1) = 1, and F(n) = F(n-1) + F(n-2)

#While Loop
def whileFib():
	f1 = 1
	f2 = 0
	term = int(input("How many terms?:\n"))
	print("The first " + str(term) + " terms of the Fibonacci Sequence:\n")
	fibo = 0
	i = 0
	while (i < term):
		if (i == 0 or i == 1):
			print(i)
		else:
			fibo = f1 + f2
			print(fibo)
			f2 = f1
			f1 = fibo
		i += 1

# Recursion
def recFib():
	def fib(n):
		if (n <= 1):
			return n
		else:
			return fib(n - 1) + fib(n - 2)
	terms = int(input("How many terms?:\n"))
	if (terms <= 0):
			print("Please enter a positive integer")
			terms = int(input("How many terms?:\n"))
	print("The first " + str(terms) + " of the Fibonacci Sequence:\n")
	for i in range(terms):
		print(fib(i))

# For Loop
def forFib():
	f1 = 1
	f2 = 0
	terms = int(input("How many terms?:\n"))
	print("\nThe first " + str(terms) + " terms of the Fibonacci Sequence:\n")
	fibo = 0
	i = 0
	for i in range(terms):
		if (i == 0 or i == 1):
			print(i)
		else:
			fibo = f1 + f2
			print(fibo)
			f2 = f1
			f1 = fibo
def main():
	print("What would you like to do?")
	print("Your options are shown below:\nA. Fibonnaci\nB. Factorial")
	choice = input("What would you like to do? Enter the corresponding letter:\n").lower()
	if ( choice == 'a' ):
		print("What method would you like to use?")
		print("Here are you options:\nA. for loop\nB. while loop\nC. recursion")
		decision = input("Choose your choice and entere the corresponding letter:\n").lower()
		if (decision == 'a'):
			forFib()
		elif (decision == "b"):
			whileFib()
		elif (decision == "c"):
			recFib()
	elif (choice == "b"):
		print("What method would you like to use?")
		print("Here are your options:\nA. For loop\nB.While loop")
		decision = print('Enter your choice with the correspondig number:\n').lower()
		if (decision == "a"):
			forFact()
		elif (decision == "b"):
			recFact()
	
if (__name__ == "__main__"):
	main()

	