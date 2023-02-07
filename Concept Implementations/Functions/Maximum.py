print("Application to find out maximum number")

def Maximum (numbers):
	return max(numbers)

def main():
	print("Enter first number:")
	no1 = input()
	print("Enter second number:")
	no2 = input()

	inputList = [int(no1), int(no2)]

	maximum = Maximum(inputList)
	maximum1 = Maximum1(int(no1), int(no2))
	print("Maximum is:"+str(maximum))
	print("Maximum1 is:"+str(maximum1))

def Maximum1 (value1, value2):
	if value1 > value2:
		return value1
	else:
		return value2

if __name__ == "__main__": # starter - call to main function
	main()

# every prg should minimum have these - starter, main func, business logic func
