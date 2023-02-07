# Program which accepts name from user and displays its length
# Input : Marvellous Output : 10
# Author : Shruti Pimparkar

def measureLength(name):
	return len(name)

def main():
	print("Enter your name:")
	print(str(measureLength(input())))

if __name__ == "__main__":
	main()