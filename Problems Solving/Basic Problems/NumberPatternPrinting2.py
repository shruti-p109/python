# Program which accepts one number and displays below pattern
# Input: 5
# Output : 1 
#		   1 2
#		   1 2 3 
#		   1 2 3 4 
#		   1 2 3 4 5
# Author : Shruti Pimparkar

def displayPattern(number):
	for i in range(1,number+1): # i = 1 2 3 4 5
		for j in range(1,i+1): # for i=1 print 1, for i=2 print 1 2, for i=3 print 1 2 3 ....
			print(j, end=" ")
		print() # new line after each row

def main():
	print("Enter a number:")
	displayPattern(int(input()))

if __name__ == "__main__":
	main()