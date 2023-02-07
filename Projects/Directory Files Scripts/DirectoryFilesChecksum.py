# Author : 				Shruti Pimparkar
# Problem Statement : 	File IO - Log checksum of all files in given directory

import os
from sys import *
import datetime
import hashlib

# read file in BlockSize chunks
def GenerateCheckSum1(File, BlockSize = 1024):
	with open(File, mode = "rb") as fp:
		Hasher = hashlib.sha256()
		Buffer = fp.read(BlockSize)
		if len(Buffer) > 0:
			Hasher.update(Buffer)
			Buffer = fp.read(BlockSize)
		return Hasher.hexdigest()

def GenerateChecksum(File):
	# with syntax - takes care of cleanup such as closing the file
	with open(File, mode = "rb") as FileHandle:
		return hashlib.sha256(FileHandle.read()).hexdigest()

def GetFilesChecksum(DirectoryPath):
	# validate path
	if not os.path.exists(DirectoryPath):
		return "Error: {} does not exist.".format(DirectoryPath)

	try:
		FilesList = list()
		for DirPath, SubDirPaths, Files in os.walk(DirectoryPath):
			for File in Files:
				FilesList.append("{} checksum : {}\n".format(File, GenerateChecksum(os.path.join(DirPath, File))))
		if FilesList:
			return FilesList
	except Exception as ex:
		return "Getting checksum failed: " + str(ex)

def main():
	FileOutput = None
	if len(argv) != 2:
		FileOutput = "Error: Invalid no. of arguments, script not executed. Sample Correct Usage: DirectoryFilesChecksum.py Demo"
	else:
		FileOutput = GetFilesChecksum(argv[1])
	
	if FileOutput:
		try:
			FileHandle = open(datetime.datetime.now().strftime("DirectoryFilesChecksumOutput_%d-%m-%Y_%H-%M-%S.txt"), "w", encoding = "utf-8")
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