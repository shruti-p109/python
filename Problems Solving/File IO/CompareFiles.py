# Author : 				Shruti Pimparkar
# Problem Statement : 	File IO - Compare two files

import os
from filecmp import cmp

def CompareFiles(FileName1, FileName2):
	if os.path.exists(FileName1) and os.path.exists(FileName2):
		if cmp(FileName1, FileName2, shallow = False): # shallow - default True - treat files as identical if their stat signatures (type, size, mtime) are identical. Otherwise, files are considered different if their sizes or contents differ.
			print("Files contents is same.")
		else:
			print("Files contents are different.")
	else:
		print("Either", FileName1, "or", FileName2, "do not exist.")

def main():
	print("Enter first file name:")
	Name1 = input()
	print("Enter second file name:")
	Name2 = input()

	CompareFiles(Name1, Name2)

if __name__ == "__main__":
	main()
