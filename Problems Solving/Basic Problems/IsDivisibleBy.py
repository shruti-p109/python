# Fucntion which accepts number one number from user and returns true if its divisible by 5 otherwise returns false
# Input : 25  Output : True
# Input : 8   Output : False
# Author : Shruti Pimparkar

def isDivisibleBy5(number):
	if number % 5 == 0:
		return True
	else:
		return False

def main():
	print("Enter Number:")
	number = input()
	if(isDivisibleBy5(int(number))):
		print("True")
	else:
		print("False")

if __name__ == "__main__":
	main()