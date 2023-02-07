# Function which accepts 2 numbers and returns their sum
# Input : 11 5 Output : 16
# Author : Shruti Pimparkar

def Add(number1, number2):
	return number1 + number2

def main():
	print("Enter two Numbers to add:")
	# split() - method of str class, splits string according separator given as argument, default separator is space
	# input() - outputs object of str class
	numbers = input().split(" ") # or numbers = input().split()
	# validation
	if len(numbers) != 2:
		print("Invalid number of inputs. Please Enter exactly 2 numbers.")
		exit()
	print(Add(int(numbers[0]), int(numbers[1])))

if __name__ == "__main__":
	main()