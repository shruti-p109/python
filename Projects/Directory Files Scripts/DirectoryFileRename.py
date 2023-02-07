# Author : 				Shruti Pimparkar
# Problem Statement : 	File IO - Search & rename files with given extension by other given extension

import os
from sys import *
import datetime

def RenameFilesByExtension(DirectoryPath, Extension, RenameExtension):
	# validate path
	if not os.path.exists(DirectoryPath):
		return "{} does not exist.".format(DirectoryPath)

	try:
		FilesList = list()
		for DirPath, SubDirPaths, Files in os.walk(DirectoryPath):
			for File in Files:
				if File.endswith(Extension):
					# absolute path of renamed file
					RenamedFile = os.path.join(DirPath, os.path.splitext(File)[0] + RenameExtension)
					# absolute path of original file & renamed file
					os.rename(os.path.join(DirPath, File), RenamedFile)
					FilesList.append("{} renamed to {}\n".format(os.path.join(DirPath, File), RenamedFile))
		if FilesList:
			return FilesList
	except Exception as ex:
		return "Rename failed: " + str(ex)

def main():
	FileOutput = None
	if len(argv) != 4:
		FileOutput = "Error: Invalid no. of arguments, script not executed. Sample Correct Usage: DirectoryFileRename.py Demo .txt .doc"
	else:
		FileOutput = RenameFilesByExtension(argv[1], argv[2], argv[3])
	
	if FileOutput:
		try:
			FileHandle = open(datetime.datetime.now().strftime("DirectoryFileRenameOutput_%d-%m-%Y_%H-%M-%S.txt"), "w", encoding = "utf-8")
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