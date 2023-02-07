# Program which accepts number from user and prints that many number "*" on screen
# Input : 5  Output : * * * * *
# Author : Shruti Pimparkar

def displayPattern(limit):
	for i in range(limit):
		print("* ", end = "")

def main():
	print("Enter Number:")
	number = input()
	displayPattern(int(number))

if __name__ == "__main__":
	main()