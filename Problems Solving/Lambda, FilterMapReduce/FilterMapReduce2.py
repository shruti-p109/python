# Program with filter - >=70 and <=90 only, map - Increment by 10, reduce - their product
# Author : Shruti Pimparkar

from functools import reduce

FilterFunc = lambda No : No >= 70 and No <=90

MapIncrement = lambda No : No + 10

ReduceToProduct = lambda No1, No2 : No1 * No2

def AcceptListFromUser():
	print("Enter no of elements:")
	size = int(input())
	InputElements = list()
	for i in range(1,size+1):
		print("Enter element ",i,":")
		InputElements.append(int(input()))
	return InputElements

def main():
	# InputList = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
	InputList = AcceptListFromUser()
	print("Data",InputList)

	# filter - >=70 and <=90 only
	InputListFilter = list(filter(FilterFunc, InputList))
	print("Data after Filter", InputListFilter)
	if len(InputListFilter) == 0: # reduce gives error on empty input list so added validation after filter
		print("Filter list found empty, nothing to map and reduce")
		exit()

	# map - Increment by 10
	InputListMap = list(map(MapIncrement, InputListFilter))
	print("Data after Map", InputListMap)

	# reduce - their product
	InputListReduce = reduce(ReduceToProduct, InputListMap)
	print("Data after Reduce", InputListReduce)

# starter
if __name__ == "__main__":
	main()