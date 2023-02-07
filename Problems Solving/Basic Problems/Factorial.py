# Program which accepts one number and returns its factorial
# Input: 5 Output : 120
# Author : Shruti Pimparkar

def factorial(number):
	fact = 1
	for i in range(number,0,-1):
		fact *= i
	return fact

def main():
	print("Enter a number:")
	number = int(input())
	print("Factorial of",number,"is",factorial(number))

if __name__ == "__main__":
	main()