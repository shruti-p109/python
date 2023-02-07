# Program which accepts one number and displays number of digits in that number
# Input: 5125623
# Output : 7
# Author : Shruti Pimparkar

def numberOfDigits(number):
	# alternative is iterating and counting each digit
	return len(number)

def main():
	print("Enter a number:")
	# input() by default outputs a string, just measure its length using len()
	# strip method of str class called on input() to avoid counting spaces
	print(str(numberOfDigits(input().strip())))

if __name__ == "__main__":
	main()