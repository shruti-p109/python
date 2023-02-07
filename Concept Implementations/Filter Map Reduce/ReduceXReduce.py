# Filter Map Reduce - there in built functions for all 3 - in this prog - same in our own user defined functions filterX, mapX, reduceX
# Author : Shruti Pimparkar

from functools import reduce

# def IsEven(No):
# 	return No % 2 == 0

IsEven = lambda No : No % 2 == 0 # preferred using this over directly writing lambda fucntion as param inside filter, map , reduce

# def Double(No):
# 	return No * 2

Double = lambda No : No * 2

def Product(No1, No2):
	return No1 * No2

# Product = lambda No1, No2 : No1 * No2

def filterX(Func_name, InputList):
	InputListFiltered = list()
	for No in InputList:
		if Func_name(No):
			InputListFiltered.append(No)
	return InputListFiltered

def mapX(Func_name, InputList):
	InputListMapped = list()
	for No in InputList:
		InputListMapped.append(Func_name(No))
	return InputListMapped

def reduceX(Func_name, InputList):
	Result = InputList[0]
	for i in range(1,len(InputList)):
		Result = Func_name(Result, InputList[i])
	return Result

def AcceptListFromUser():
	print("Enter number of elements:")
	Size = int(input())
	if Size <=0 :
		print("Number of elements can not be zero or negative")
		exit()
	InputList = list()
	for i in range(1, Size+1):
		print("Enter element", i)
		InputList.append(int(input()))
	return InputList

def main():
	InputElements = AcceptListFromUser()

	# filterX, filter
	InputElementsFilterX = filterX(IsEven, InputElements)
	print("Output after filterX",InputElementsFilterX)

	InputElementsFilterXLambda = filterX(lambda No : No % 2 == 0, InputElements)
	print("Output after filterX using lambda function",InputElementsFilterXLambda)

	InputElementsFilter = list(filter(IsEven, InputElements)) # if you don't typecast by list() it returns <filter object at 0x0000028A79C27E80>
	print("Output after in-built filter",InputElementsFilter)

	InputElementsFilterLambda = list(filter(lambda No : No % 2 == 0, InputElements))
	print("Output after in-built filter using lambda function",InputElementsFilterLambda)

	print("===============================")

	# mapX, map
	InputElementsMapX = mapX(Double, InputElementsFilterX)
	print("Output after mapX",InputElementsMapX)

	InputElementsMapXLambda = mapX(lambda No : No * 2, InputElementsFilterXLambda)
	print("Output after mapX using lambda function",InputElementsMapXLambda)

	InputElementsMap = list(map(Double, InputElementsFilter)) # if you don't typecast by list() it returns <map object at 0x000002324D237D60>
	print("Output after in-built map",InputElementsMap)

	InputElementsMapLambda = list(map(lambda No : No * 2, InputElementsFilterLambda))
	print("Output after in-built map using lambda function",InputElementsMapLambda)

	print("===============================")

	# reduceX, reduce
	InputElementsReduceX = reduceX(Product, InputElementsMapX)
	print("Output after reduceX",InputElementsReduceX)

	InputElementsReduceXLambda = reduceX(lambda No1, No2 : No1 * No2, InputElementsMapXLambda)
	print("Output after reduceX using lambda function",InputElementsReduceXLambda)

	InputElementsReduce = reduce(Product, InputElementsMap)
	print("Output after in-built reduce",InputElementsReduce) # NameError: name 'reduce' is not defined. Did you mean: 'reduceX'?
	# reduce has dependency, need to import it from functools module

	InputElementsReduceLambda = reduce(lambda No1, No2 : No1 * No2, InputElementsMapLambda)
	print("Output after in-built reduce using lambda function",InputElementsReduceLambda)

	# all 3 at once
	print("one line FMR:",reduce(lambda No1, No2 : No1 * No2, list(map(lambda No : No * 2, list(filter(lambda No : No % 2 == 0, InputElements))))))
	
# starter - from where execution starts
if 	__name__ == "__main__":
	main()
