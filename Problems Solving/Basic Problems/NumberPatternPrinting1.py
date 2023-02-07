# Program which accepts one number and displays below pattern
# Input: 5
# Output : 1 2 3 4 5
#		   1 2 3 4 5
#		   1 2 3 4 5
#		   1 2 3 4 5
#		   1 2 3 4 5
# Author : Shruti Pimparkar

def displayPattern(number):
	for i in range(number): # 5 rows
		for j in range(1,number+1): # for each row print 1-5
			print(j, end=" ")
		print() # new line after each row

def main():
	print("Enter a number:")
	displayPattern(int(input()))

if __name__ == "__main__":
	main()