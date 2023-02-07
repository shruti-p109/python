# Program which accepts one number and displays addition of digits in that number
# Input: 5187934
# Output : 37
# Author : Shruti Pimparkar

def additionOfDigits(number):
	sum = 0
	for i in number:
		sum += int(i) # convert each digit to int before adding to sum
	return sum

def main():
	print("Enter a number:")
	# input() returns string, so call strip() on it to remove spaces if any
	print(additionOfDigits(input().strip()))

if __name__ == "__main__":
	main()