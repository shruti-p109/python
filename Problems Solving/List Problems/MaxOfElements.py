# Program which accepts N numbers of inputs from user & stores it in list & returns max of list
# Input: Number of elements :6
# Input Elements: 11 5 45 7 4 56
# Output : 56
# Author : Shruti Pimparkar

def maxOfListElements(inputList):
	return max(inputList)

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
	Maximum = maxOfListElements(inputList)
	print("Maximum of input elements is :", Maximum)

if __name__ == "__main__":
	main()