# Program which accepts number from user and checks if its 0 or positive or negative
# Input : -11 Output : Negative Number
# Input : 8   Output : Negative Number
# Input : 0   Output : Zero
# Author : Shruti Pimparkar

def positiveNegative(number):
	if number > 0:
		print("Positive Number")
	elif number < 0:
		print("Negative Number")
	else:
		print("Zero")

def main():
	print("Enter Number:")
	number = input()
	positiveNegative(int(number))

if __name__ == "__main__":
	main()