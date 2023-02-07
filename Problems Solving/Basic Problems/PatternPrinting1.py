# Program which displays below pattern
# Input: 5
# Output: * * * * *
# 		  * * * * *
# 		  * * * * *
# 		  * * * * *
# 		  * * * * *
# Author : Shruti Pimparkar

def displayPattern(limit):
	for i in range(limit):
		for i in range(limit):
			print("*", end=" ")
		print()

def main():
	print("Enter a number:")
	displayPattern(int(input()))

if __name__ == "__main__":
	main()