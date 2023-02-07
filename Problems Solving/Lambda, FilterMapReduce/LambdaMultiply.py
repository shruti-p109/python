# Program containing 1 lambda function which accepts 2 parameters and returns their multiplication
# Input: 4 3 Output: 12
# Author : Shruti Pimparkar

def main():
	print("Enter number 1:")
	No1 = int(input())
	print("Enter number 2:")
	No2 = int(input())
	Multiply = lambda No1, No2 : No1 * No2
	Ans = Multiply(No1, No2)
	print("Multiplication is",Ans)

if __name__ == "__main__":
	main()