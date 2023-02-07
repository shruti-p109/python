# Author : 				Shruti Pimparkar
# Problem Statement : 	Multithreading

import threading

# Display addition of even nos in list
def EvenList(InputList):
	Sum = 0
	for No in InputList:
		if No % 2 == 0:
			print("Even in list:", No)
			Sum += No
	print("Sum of Even nos in list is", Sum)

# Display addition of odd nos in list
def OddList(InputList):
	Sum = 0
	for No in InputList:
		if No % 2 != 0:
			print("Odd in list:", No)
			Sum += No
	print("Sum of Odd nos in list is", Sum)

def main():
	Inputlist = [2,6,1,11,49,12,22,35]
	Evenlist = threading.Thread(target = EvenList, args = (Inputlist,))
	Oddlist = threading.Thread(target = OddList, args = (Inputlist,))

	Evenlist.start()
	Oddlist.start()

	Evenlist.join()
	Oddlist.join()

	print("exit from main")

if __name__ == "__main__":
	main()

