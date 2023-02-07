# Author : 				Shruti Pimparkar
# Problem Statement : 	File IO - Copy files from given directory, create given directory, paste all files there

import os
from sys import *
import datetime
import shutil

def CopyFilesByExtension(SrcDirectoryPath, DestDirectoryPath, Extension):
	# validate path
	if not os.path.exists(SrcDirectoryPath):
		return "{} does not exist.".format(SrcDirectoryPath)

	try:
		FilesList = list()

		# create directory
		if not os.path.exists(DestDirectoryPath):
			os.makedirs(DestDirectoryPath)

		for DirPath, SubDirPaths, Files in os.walk(SrcDirectoryPath):
			for File in Files:
				if File.endswith(Extension):
					shutil.copy(os.path.join(DirPath, File), DestDirectoryPath)
					FilesList.append("{} copied to {}\n".format(os.path.join(DirPath, File), os.path.join(DestDirectoryPath, File)))
		if FilesList:
			return FilesList
		else:
			# delete created folder
			os.rmdir(DestDirectoryPath) # removes only empty directory - scope for improvement ??
	except Exception as ex:
		os.rmdir(DestDirectoryPath)
		return "Copying files by extension failed: " + str(ex)

def main():
	FileOutput = None
	if len(argv) != 4:
		FileOutput = "Error: Invalid no. of arguments, script not executed. Sample Correct Usage: DirectoryCopyFilesByExtension.py Demo Temp .py"
	else:
		FileOutput = CopyFilesByExtension(argv[1], argv[2], argv[3])
	
	if FileOutput:
		try:
			FileHandle = open(datetime.datetime.now().strftime("DirectoryCopyFilesByExtensionOutput_%d-%m-%Y_%H-%M-%S.txt"), "w", encoding = "utf-8")
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