# Author : 				Shruti Pimparkar
# Problem Statement : 	Multithreading

import threading

# Display 1st 10 even numbers
def DisplayEven(No):
	for i in range(No*2):
		if i % 2 == 0:
			print("Even Number:", i)

# Display 1st 10 odd numbers
def DisplayOdd(No):
	for i in range(No*2):
		if i % 2 != 0:
			print("Odd Number:", i)

def main():
	Number = 10
	even = threading.Thread(target = DisplayEven, args = (Number,))
	odd = threading.Thread(target = DisplayOdd, args = (Number,))

	even.start()
	odd.start()

	even.join()
	odd.join()

	print("End of main")

if __name__ == "__main__":
	main()

