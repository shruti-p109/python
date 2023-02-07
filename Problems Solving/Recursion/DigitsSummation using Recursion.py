# Author : 				Shruti Pimparkar
# Problem Statement : 	Recursion

def DigitsSummation(No):
	Sum = 0
	while No > 0:
		Sum += No % 10
		No //= 10
	return Sum

def DigitsSummationR(No):
	if No > 0:
		return (No % 10) + DigitsSummationR(No//10)
	else:
		return 0

def main():
	print("Enter a number:")
	Number = int(input())
	print("--- By Iterative Approach ---")
	print("Sumation of digits is", DigitsSummation(Number))
	print("\n--- By Recursive Approach ---")
	print("Sumation of digits is", DigitsSummationR(Number))

if __name__ == "__main__":
	main()