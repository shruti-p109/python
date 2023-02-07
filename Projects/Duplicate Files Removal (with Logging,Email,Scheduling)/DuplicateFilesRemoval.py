from sys import *
import os
import datetime
import time
import schedule
import re
import FileFunctions
import EmailFunctionality

def DeleteDuplicateFiles(DirectoryPath):
	# validate path
	if not os.path.exists(DirectoryPath):
		return "Error: Directory {} does not exist.".format(DirectoryPath)

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
					CurrentFileFullChecksum = FileFunctions.GenerateChecksum(AbsFilePath)
					# compare its checksum with all the same size files checksum
					for SameSizeFileDict in FileSizeDict[CurrentFileSize]: 
						# generate & update checksum of SameSizeFile if it is None (for possible future re-use)
						if not SameSizeFileDict["checksum"]:
							SameSizeFileDict["checksum"] = FileFunctions.GenerateChecksum(SameSizeFileDict["path"])
						if CurrentFileFullChecksum == SameSizeFileDict["checksum"]:
							# duplicate file
							DuplicateFilesList.append(AbsFilePath + "\n")
							# delete duplicate file
							os.remove(AbsFilePath)
						else:
							# add to list of same size files
							FileSizeDict[CurrentFileSize].append({"path": AbsFilePath, "checksum": CurrentFileFullChecksum})
				else:
					# create and add to list of same size files
					FileSizeDict[CurrentFileSize] = [{"path": AbsFilePath, "checksum": None}] 
		if DuplicateFilesList:
			return DuplicateFilesList
	except Exception as ex:
		return "Getting & deleting duplicate files failed: " + str(ex)

def ValidateArguments(Arguments):
	InvalidEmailError = False

	if len(Arguments) >= 4 and not re.fullmatch(r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+", Arguments[3]):
		InvalidEmailError = True
		return "Error: Invalid Email {}".format(Arguments[3]), InvalidEmailError

	if len(Arguments) != 4:
		return "Error: Invalid no. of arguments. Sample Correct Usage: 'DuplicateFilesRemoval.py Demo 50 email_id_1,email_id_2'. 50 is time interval in minutes for task scheduling. For multiple email ids, make sure to add them comma (without space) separated.", InvalidEmailError

	return None, InvalidEmailError

def DuplicateFilesRemovalTasks(CommandLineArgs, LogFileName):
	# validation
	FileOutput, InvalidEmail = ValidateArguments(CommandLineArgs)
	if not FileOutput:
		FileOutput = DeleteDuplicateFiles(CommandLineArgs[1])
	
	# write output in log file
	if FileOutput:
		if isinstance(FileOutput, list):
			Header = "-" * 20 + "\nBelow are duplicate files that were deleted on "+ time.ctime() + ":\n"
			FileOutput.insert(0, Header)
		LogFilePath, LogTimeForMail = FileFunctions.WriteOutputLog(FileOutput, LogFileName)
	# mail the log file - argv[3]
	if FileOutput and LogFilePath and not InvalidEmail:
		Result = EmailFunctionality.SendTxtAttachmentMail ("spython188@gmail.com", CommandLineArgs[3].split(","), "Duplicate Files Cleaning Log for " + LogTimeForMail , "Hello, This is a test mail.<br>Please find Log file in the attachment for duplicate files deleted on <b>" + LogTimeForMail + "</b>.\n", "zpvvpuuvlfgisvwo", [LogFilePath])
		if not Result[0]:
			FileFunctions.WriteOutputLog(Result[1], LogFileName)
		
def main():
	if argv[1] == "-h" or argv[1] == "-H":
		print("This script is used to delete duplicate files in given directory & mail the log file to given mail id at given interval.")
		exit()

	if argv[1] == "-u" or argv[1] == "-U":
		print("Usage : application_name directory_path schedule_time_in_minutes email_id1,email_id2")
		exit()

	try:
		schedule.every(int(argv[2])).minutes.do(DuplicateFilesRemovalTasks, argv, datetime.datetime.now().strftime("DuplicateFileCleanUpLog_%d-%m-%Y_%H-%M-%S.txt"))

		while(True):
			schedule.run_pending()
			time.sleep(1)

	except ValueError:
		FileFunctions.WriteOutputLog("Failed to execute task: Invalid datatype of input.", datetime.datetime.now().strftime("DuplicateFileCleanUpLog_%d-%m-%Y_%H-%M-%S.txt"))

if __name__ == "__main__":
	main()