# Author : 				Shruti Pimparkar
# Problem Statement : 	File IO - Write (in file) names of files in given directory with give extension 

import os
from sys import argv
from pathlib import suffix
import datetime

def GetFilesByExtension(DirectoryPath, Extension):
	if os.path.exists(DirectoryPath):
		print("Given Directory Path exists.")
		for None, None, FileNames in os.walk(DirectoryPath):
			for FileName in FileNames:
				print(FileName)
	else:
		raise Exception("Given Directory Path does not exist.")

def main():
	# create file for writing
	fileHandle = None
	try:
		fileHandle = open(datetime.datetime.now().strftime("DirectoryFileSearchOutput_%d-%m-%Y_%H-%M-%S.txt"), "w", encoding = "utf-8")
		if len(argv) != 3:
			fileHandle.write("Error: Insufficient arguments, script not executed. Sample Correct Usage: DirectoryFileSearch.py Demo .txt")
		else:
			GetFilesByExtension(argv[1], argv[2])
	except Exception as ex:
		if fileHandle:
			fileHandle.write("Exception thrown during script execution: {}".format(ex.args))
	finally:
		print("Inside finally.")
		if fileHandle:
			fileHandle.close()

if __name__ == "__main__":
	main()