# Program which accepts N numbers of inputs from user & stores it in list, accepts one number & retuns its frequency in list
# Input: Number of elements :6
# Input Elements: 11 5 4 7 4 56
# Frequency Number : 4
# Output : 2
# Author : Shruti Pimparkar

def FreqOfNo(InputList, No):
	freq = 0
	for InputNo in InputList:
		if InputNo == No:
			freq += 1
	return freq

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
	print("Enter number to find frequency of:")
	FreqNumber = int(input())
	Frequency = FreqOfNo(inputList, FreqNumber)
	print("Frequency of",FreqNumber,"in input elements is :", Frequency)

if __name__ == "__main__":
	main()