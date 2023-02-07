# Program with filter - even only, map - square, reduce - addition
# Author : Shruti Pimparkar

from functools import reduce

# filter helper function
IsEven = lambda No : No % 2 == 0

# map helper function
Square = lambda No : No * No

# reduce helper function
Add = lambda No1, No2 : No1 + No2

def AcceptListFromUser():
	print("Enter no of elements:")
	size = int(input())
	InputElements = list()
	for i in range(1,size+1):
		print("Enter element ",i,":")
		InputElements.append(int(input()))
	return InputElements

def main():
	# InputList = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
	InputList = AcceptListFromUser()
	print("Data",InputList)

	# filter - even only
	InputListFilter = list(filter(IsEven, InputList))
	print("Data after Filter", InputListFilter)
	if len(InputListFilter) == 0: # reduce gives error on empty input list so added validation after filter
		print("Filter list found empty, nothing to map and reduce")
		exit()

	# map - square
	InputListMap = list(map(Square, InputListFilter))
	print("Data after Map", InputListMap)

	# reduce - addition
	InputListReduce = reduce(Add, InputListMap)
	print("Data after Reduce", InputListReduce)

# starter
if __name__ == "__main__":
	main()