# Program which accepts N numbers of inputs from user & stores it in list & returns addition of all elements of list
# Input: Number of elements :6
# Input Elements: 11 5 45  7 4 56
# Output : 130
# Author : Shruti Pimparkar

def AddListElements(inputList):
	Sum = 0
	for no in inputList:
		Sum += no
	return Sum

def main():
	print("Enter Number of Input Elements:")
	size = int(input())
	if size <= 0:
		print("Error : Number of input elements can be negative or zero")
		exit()
	inputList = []
	print("Enter",size,"Input Elements one by one:")
	for i in range(1,size+1):
		print("Enter Element",i)
		inputList.append(int(input()))
	addition = AddListElements(inputList)
	print("Addition of input elements is :",addition)

if __name__ == "__main__":
	main()