# Author : 				Shruti Pimparkar
# Problem Statement : 	Recursion

def Factorial(No):
	Fact = 1
	while No > 1:
		Fact *= No
		No -= 1
	return Fact

def FactorialR(No):
	if No > 1:
		return No * FactorialR(No-1)
	else:
		return 1

def main():
	print("Enter a number:")
	Number = int(input())
	print("--- By Iterative Approach ---")
	print("Factorial is", Factorial(Number))
	print("\n--- By Recursive Approach ---")
	print("Factorial is", FactorialR(Number))

if __name__ == "__main__":
	main()