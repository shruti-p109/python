# Author		   : Shruti Pimparkar
# Problem Statement: Traverse given directory fully (nesting included) and display information of each file - like dir or ls command (but this only goes 1 level down)

# executing by realtive path : python DirectoryWatcherScript.py A
# executing by absolute path : python DirectoryWatcherScript.py "C:\Users\shruti\Desktop\Marvellous Infosystems - Python ML Batch\Lectures\Lecture 15 - 13-11-22\Programs\A"

import os
from sys import *

def TraverseDirectory(DirectoryPath):
	print("Inside TraverseDirectory, DirectoryPath is", DirectoryPath)

	Result = os.walk(DirectoryPath);
	# print(type(Result)) # <class 'generator'> - check
	for DirPath, SubDirPaths, FileNames in Result:
		print("Directory Name:", DirPath)
		for SubDirPath in SubDirPaths:
			print("Sub Directory Name:", SubDirPath)
		for FileName in FileNames:
			print("File in directory {}:".format(DirPath), FileName)

def main():
	print("---- Directory Watcher Script ----")

	if len(argv) != 2:
			print("Error :Insufficient arguments. Use -h for help and -u for usage of script")
			print("Use -h for help and -u for usage of script")
			exit()

	if argv[1] == "-h" or argv[1] == "-H":
		print("This script is used to traverse given directory fully (nesting included) and display information of each file.")
		exit()

	if argv[1] == "-u" or argv[1] == "-U":
		print("Usage : application_name directory_path")
		exit()

	TraverseDirectory(argv[1])

if __name__ == "__main__":
	main()