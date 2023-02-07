# Program containing 1 lambda function which accepts 1 parameter and returns power of 2
# Input: 4 Output: 16
# Author : Shruti Pimparkar

def main():
	print("Enter a number:")
	power = int(input())
	PowerOfTwo = lambda No : 2**No
	Ans = PowerOfTwo(power)
	print("2 raised to",power,"is",Ans)

if __name__ == "__main__":
	main()