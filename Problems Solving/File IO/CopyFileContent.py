# Author : 				Shruti Pimparkar
# Problem Statement : 	File IO - Open file, copy its content in another newly created file

import os

def CopyFileContent(FileName):
	if os.path.exists(FileName):
		if os.path.getsize(FileName) == 0:
			print(FileName, "file is empty.")
		else:
			try:
				fileHandle = open(FileName, mode = "r", encoding = "utf-8")
				newFileHandle = open("Demo.txt", mode = "w", encoding = "utf-8")

				newFileHandle.write(fileHandle.read())
				print("Done")
			finally:
				fileHandle.close()
				newFileHandle.close()
	else:
		print("File does not exist.")

def main():
	print("Enter file name to copy content from:")
	Name = input()

	CopyFileContent(Name)

if __name__ == "__main__":
	main()
