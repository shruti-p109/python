# Author : 				Shruti Pimparkar
# Problem Statement : 	Multithreading

import threading

# count of small case letters from string
def SmallCaseCount(InputString):
	print("Small Thread Name is {} & ID is {}".format(threading.current_thread().name, threading.get_native_id()))
	Sum = 0
	for Char in InputString:
		if Char.islower():
			print("Lower Character:", Char)
			Sum += 1
	print("Count of small letters in string is", Sum)

# count of upper case letters from string
def UpperCaseCount(InputString):
	print("Capital Thread Name is {} & ID is {}".format(threading.current_thread().name, threading.get_native_id()))
	Sum = 0
	for Char in InputString:
		if Char.isupper():
			print("Upper Character:", Char)
			Sum += 1
	print("Count of capital letters in string is", Sum)

# count of digits from string
def DigitCount(InputString):
	print("Digit Thread Name is {} & ID is {}".format(threading.current_thread().name, threading.get_native_id()))
	Sum = 0
	for Char in InputString:
		if Char.isdigit():
			print("Digit:", Char)
			Sum += 1
	print("Count of digits in string is", Sum)

def main():
	Inputstring = "Shruti526"
	Small = threading.Thread(target = SmallCaseCount, args = (Inputstring,))
	Capital = threading.Thread(target = UpperCaseCount, args = (Inputstring,))
	Digits = threading.Thread(target = DigitCount, args = (Inputstring,))

	Small.start()
	Capital.start()
	Digits.start()

	Small.join()
	Capital.join()
	Digits.join()

	print("exit from main")

if __name__ == "__main__":
	main()

