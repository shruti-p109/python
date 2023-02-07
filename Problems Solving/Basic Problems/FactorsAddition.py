# Program which accepts one number and returns its addition of its factors
# Input: 12 Output : 16 (1+2+3+4+6)
# Author : Shruti Pimparkar

# return addition of factors except the number itself
def factorsAddition(number):
	# initialized to 1 as 1 ia always going to be factors of any number
	sum = 1
	# print("1")
	for i in range(2,int(number/2)+1):
		if number % i == 0:
			# print(i)
			# i is a factor of number, add it to sum
			sum += i
	return sum

def main():
	print("Enter a number:")
	number = int(input())
	print("Addition of factors of",number,"is",factorsAddition(number))

if __name__ == "__main__":
	main()