# Filter Map Reduce - there in built functions for all 3 - in this prog - same in our own user defined functions filterX, mapX, reduceX
# Author : Shruti Pimparkar

def IsEven(No):
	return No % 2 == 0

def Double(No):
	return No * 2

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

	# mapX, map
	InputElementsMapX = mapX(Double, InputElementsFilterX)
	print("Output after mapX",InputElementsMapX)

	InputElementsMapXLambda = list(mapX(lambda No : No * 2, InputElements))
	print("Output after mapX using lambda function",InputElementsMapXLambda)

	
# starter - from where execution starts
if 	__name__ == "__main__":
	main()
