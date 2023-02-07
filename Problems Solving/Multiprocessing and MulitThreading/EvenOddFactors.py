# Author : 				Shruti Pimparkar
# Problem Statement : 	Multithreading

import threading

# Display addition of even factors
def EvenFactors(No):
	Sum = 0
	for i in range(1, int(No / 2) + 1):
		if No % i == 0 and i % 2 == 0:
			print("Even factor:",i)
			Sum += i
	print("Sum of Even Factors is", Sum)

# Display addition of odd factors
def OddFactors(No):
	Sum = 0
	for i in range(1, int(No / 2) + 1):
		if No % i == 0 and i % 2 != 0:
			print("Odd factor:",i)
			Sum += i
	print("Sum of Odd Factors is", Sum)

def main():
	Number = 100
	Evenfactor = threading.Thread(target = EvenFactors, args = (Number,))
	OddFactor = threading.Thread(target = OddFactors, args = (Number,))

	Evenfactor.start()
	OddFactor.start()

	Evenfactor.join()
	OddFactor.join()

	print("exit from main")

if __name__ == "__main__":
	main()

