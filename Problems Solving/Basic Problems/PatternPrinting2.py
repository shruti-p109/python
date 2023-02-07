# Program which accepts one number and displays below pattern
# Input: 5
# Output : * * * * *
#		   * * * *
#		   * * *
#		   * *
#		   *
# Author : Shruti Pimparkar

def displayPattern(number):
	for i in range(number,0,-1): # 5 4 3 2 1
		for j in range(i): # print * 5 times, 4 times, 3 times, 2 times, 1 times
			print("*", end=" ")
		print() # new line before decrementing

def main():
	print("Enter a number:")
	displayPattern(int(input()))

if __name__ == "__main__":
	main()