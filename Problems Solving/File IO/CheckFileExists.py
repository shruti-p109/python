# Author : 				Shruti Pimparkar
# Problem Statement : 	File IO - Check if given file exists

import os

def CheckFileExists(FileName):
	if os.path.exists(FileName):
		print("File exists.")
	else:
		print("File does not exist.")

def main():
	print("Enter file name to check in current directory:")
	Name = input()

	CheckFileExists(Name)

if __name__ == "__main__":
	main()