# Program which displays 10 to 1 on screen
# Output : 10 9 8 7 6 5  4 3 2 1
# Author : Shruti Pimparkar

def displaySequence(fromNo):
	for i in range(fromNo,0,-1):
		print(i, end=" ")

def main():
	displaySequence(10)

if __name__ == "__main__":
	main()