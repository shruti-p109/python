# Function which accepts number as input and prints if its even or odd
# Input : 11 Output : Odd Number
# INput : 8 Output : Even Number
# Author : Shruti Pimparkar

def ChkNum(number):
	if number % 2 == 0:
		print("Even Number")
	else:
		print("Odd Number")

def main():
	print("Enter Number:")
	number = input()
	ChkNum(int(number))

if __name__ == "__main__":
	main()