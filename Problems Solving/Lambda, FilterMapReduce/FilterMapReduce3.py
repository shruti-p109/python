# Program with filter - prime only, map - multiply by 2, reduce - maximum
# Author : Shruti Pimparkar

from functools import reduce

# filter helper function
def IsPrime(No):
	for i in range(2, int(No/2)+1):
		if No % i == 0:
			return False
	return True

# map helper function
Multiply = lambda No : No * 2

# reduce helper function
Max = lambda No1, No2 : max(No1, No2)

def AcceptListFromUser():
	print("Enter no of elements:")
	size = int(input())
	InputElements = list()
	for i in range(1,size+1):
		print("Enter element ",i,":")
		InputElements.append(int(input()))
	return InputElements

def main():
	# InputList = [2, 70, 11, 10, 17, 23, 31, 77]
	InputList = AcceptListFromUser()
	print("Data",InputList)

	# filter - prime only
	InputListFilter = list(filter(IsPrime, InputList))
	print("Data after Filter", InputListFilter)
	if len(InputListFilter) == 0: # reduce gives error on empty input list so added validation after filter
		print("Filter list found empty, nothing to map and reduce")
		exit()

	# map - multiply by 2
	InputListMap = list(map(Multiply, InputListFilter))
	print("Data after Map", InputListMap)
	
	# reduce - maximum
	InputListReduce = reduce(Max, InputListMap)
	print("Data after Reduce", InputListReduce)

# starter
if __name__ == "__main__":
	main()