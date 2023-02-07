# Filter Map Reduce - there in built functions for all 3 - in this prog - same in our own user defined functions filterX, mapX, reduceX
# Author : Shruti Pimparkar

def IsEven(No):
	return No % 2 == 0

def Increment(No):
	return No + 2

def filterX(Func_name, Arr):
	Result = []
	for No in Arr:
		if Func_name(No):
			Result.append(No)
	return Result

def mapX(Func_name, Arr):
	Result = []
	for No in Arr:
		Result.append(Func_name(No))
	return Result

def reduceX(Arr):
	Sum = 0
	for No in Arr:
		Sum += No
	return Sum

def main():
	Data = [2,3,1,6,4,5,11,16,20]
	print("Data", Data)
	# filter
	DataFilter = list(filterX(IsEven, Data))
	print("Data after filterX",DataFilter)
	# map - do some processing on each element of DataFilter
	DataMap = list(mapX(Increment, DataFilter))
	print("DataFilter after mapX", DataMap)
	# reduce - reduce DataMap to one number
	DataReduce = reduceX(DataMap)
	print("DataReduce after reduceX", DataReduce)

# starter - from where execution starts
if 	__name__ == "__main__":
	main()
