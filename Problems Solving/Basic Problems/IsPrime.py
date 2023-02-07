# Program which accepts one number and checks whether its prime or not
# Input: 5 Output : It is Prime Number
# Author : Shruti Pimparkar

def isPrime(number):
	for i in range(2,int(number/2)+1):
		if number % i == 0:
			# print(i)
			# found a factor other than 1 & number, so not a prime number, stop here & return false
			return False
	return True

def main():
	print("Enter a number:")
	if isPrime(int(input())):
		print("It is a Prime Number")
	else:
		print("It is not a Prime Number")

if __name__ == "__main__":
	main()