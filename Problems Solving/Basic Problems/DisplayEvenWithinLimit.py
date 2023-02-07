# Program which prints first 10 even numbers on screen
# Output : 2 4 6 8 10 12 14 16 18 20
# Author : Shruti Pimparkar

def displayEvenNumbers(limit):
	for i in range(2,2*limit+1,2):
		print(i, end=" ")

def main():
	displayEvenNumbers(10)

if __name__ == "__main__":
	main()