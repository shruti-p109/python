# Program which accepts N numbers of inputs from user & stores it in list & returns addition of prime nos of list
# Buisness logic written in MarvellousNum module
# Author : Shruti Pimparkar

from MyNum import ListPrime

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
	primeAddition = ListPrime(inputList)
	print("Addition of prime nos of list is:", primeAddition)

if __name__ == "__main__":
	main()