# Author:	Shruti Pimparkar
# Problem Statement: File IO - Delete

import os

def DeleteFile(FileName):
	if os.path.exists(FileName):
		if os.path.getsize(FileName) == 0:
			os.remove(FileName)
			print("Done")
		else:
			print("File contains some data. Are you sure you want to delete this file? Y/N")
			option = input()
			if option == "Y" or option == "y":
				os.remove(FileName)
				print("Done")
			else:
				print("File deletion aborted.")
	else:
		print("There is no such file")


def main():
	print("Enter the file name to delete:")
	Name = input()

	DeleteFile(Name)

if __name__ == "__main__":
	main()
