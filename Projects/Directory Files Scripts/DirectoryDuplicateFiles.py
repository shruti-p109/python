# Author : 				Shruti Pimparkar
# Problem Statement : 	File IO - Log names of duplicate files in given directory 

import os
from sys import *
import datetime
import hashlib

def GenerateChecksum(File, BytesToRead = None):
	# with syntax - takes care of clean-up such as closing the file
	with open(File, mode = "rb") as FileHandle:
		if BytesToRead:
			return hashlib.sha256(FileHandle.read(int(BytesToRead))).hexdigest()
		else:
			return hashlib.sha256(FileHandle.read()).hexdigest()


def GetDuplicateFiles(DirectoryPath):
	# validate path
	if not os.path.exists(DirectoryPath):
		return "Error: {} does not exist.".format(DirectoryPath)

	try:
		DuplicateFilesList = list()
		FileSizeDict = {}
		# { 
		# 	filesize1: [
		# 				{path: file1path, checksum: file1checksum (default - None)},
		# 				{path: file2path, checksum: file2checksum}
		# 			   ],
		# 	filesize2: [
		# 				{path: file3path, checksum: file3checksum},
		# 				{path: fil4path, checksum: file4checksum}
		# 			   ]
		# }
		for DirPath, SubDirPaths, Files in os.walk(DirectoryPath):
			for File in Files:
				AbsFilePath = os.path.join(DirPath, File)
				CurrentFileSize = os.path.getsize(AbsFilePath)

				if CurrentFileSize in FileSizeDict: # file found with same size
					CurrentFileFullChecksum = GenerateChecksum(AbsFilePath)
					# compare its checksum with all the same size files checksum
					for SameSizeFileDict in FileSizeDict[CurrentFileSize]: 
						# generate & update checksum of SameSizeFile if it is None (for possible future re-use)
						if not SameSizeFileDict["checksum"]:
							SameSizeFileDict["checksum"] = GenerateChecksum(SameSizeFileDict["path"])
						if CurrentFileFullChecksum == SameSizeFileDict["checksum"]:
							# duplicate file
							DuplicateFilesList.append(AbsFilePath + "\n")
						else:
							# add to list of same size files
							FileSizeDict[CurrentFileSize].append({"path": AbsFilePath, "checksum": CurrentFileFullChecksum})
				else:
					# create and add to list of same size files
					FileSizeDict[CurrentFileSize] = [{"path": AbsFilePath, "checksum": None}] 
		if DuplicateFilesList:
			return DuplicateFilesList
	except Exception as ex:
		return "Getting duplicate files failed: " + str(ex)
		
def main():
	FileOutput = None
	if len(argv) != 2:
		FileOutput = "Error: Invalid no. of arguments, script not executed. Sample Correct Usage: DirectoryDuplicateFiles.py Demo"
	else:
		FileOutput = GetDuplicateFiles(argv[1])
	
	if FileOutput:
		try:
			FileHandle = open(datetime.datetime.now().strftime("DirectoryDuplicateFilesOutput_%d-%m-%Y_%H-%M-%S.txt"), "w", encoding = "utf-8")
			if isinstance(FileOutput, list):
				FileOutput.insert(0, "Duplicate Files in {} are:\n".format(argv[1]))
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