# Author : 				Shruti Pimparkar
# Problem Statement : 	File IO - Write (in file) names of files in given directory with give extension 

import os
from sys import *
import datetime

def GetFilesByExtension(DirectoryPath, Extension):
	# validate path
	if not os.path.exists(DirectoryPath):
		return "{} does not exist.".format(DirectoryPath)

	try:
		FilesList = list()
		for DirPath, SubDirPaths, Files in os.walk(DirectoryPath):
			for File in Files:
				if File.endswith(Extension):
					FilesList.append(File + "\n")
		if FilesList:
			return FilesList
	except Exception as ex:
		return "File Search by extension failed: " + str(ex)

def main():
	FileOutput = None
	if len(argv) != 3:
		FileOutput = "Error: Invalid no. of arguments, script not executed. Sample Correct Usage: DirectoryFileSearch.py Demo .txt"
	else:
		FileOutput = GetFilesByExtension(argv[1], argv[2])
	
	if FileOutput:
		try:
			FileHandle = open(datetime.datetime.now().strftime("DirectoryFileSearchOutput_%d-%m-%Y_%H-%M-%S.txt"), "w", encoding = "utf-8")
			if isinstance(FileOutput, list):
				FileHandle.writelines(FileOutput)
			else:
				FileHandle.write(FileOutput)
		except (IOError, OSError) as ex:
			print("Failed to open/write file: "+str(ex)) # improvement ? how to handle file open/read/write exceptions in automation script?
		finally:
			if FileHandle:
				FileHandle.close()


if __name__ == "__main__":
	main()