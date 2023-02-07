# Author : 				Shruti Pimparkar
# Problem Statement : 	File IO - Open file, read content & display on screen

import os

def DisplayFileContent(FileName):
	if os.path.exists(FileName):
		if os.path.getsize(FileName) == 0:
			print("File is empty.")
		else:
			try:
				fileHandle = open(FileName, mode = "r", encoding = "utf-8") # default mode - read & text mode
				Content = fileHandle.read()
				print("File Content:")
				print(Content)
			finally: # close the file before terminating if something goes wrong
				fileHandle.close()
	else:
		print("File does not exist.")

def main():
	print("Enter file name:")
	Name = input()

	DisplayFileContent(Name)

if __name__ == "__main__":
	main()
