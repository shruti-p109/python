# Author : 				Shruti Pimparkar
# Problem Statement : 	File IO - find frequency of string in file

import os
from filecmp import cmp

def FrequencyOfAWord(FileName, StringToFind):
	if os.path.exists(FileName):
		fileHandle = open(FileName, mode = "r", encoding = "utf-8")
		FileContent = fileHandle.read() # to get frequency read full file, to only check if string exists or not, iterate line by line & break if found
		print("Frequency is:", FileContent.count(StringToFind))
	else:
		print(FileName, "does not exist.")

def main():
	print("Enter file name:")
	Name = input()
	print("Enter string to get frequency of in given file:")
	Word = input()

	FrequencyOfAWord(Name, Word)

if __name__ == "__main__":
	main()
