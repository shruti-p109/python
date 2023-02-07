from sys import *
import os
import datetime
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import schedule

def GenerateChecksum(File, BytesToRead = None):
	# with syntax - takes care of clean-up such as closing the file
	with open(File, mode = "rb") as FileHandle:
		if BytesToRead:
			return hashlib.sha256(FileHandle.read(int(BytesToRead))).hexdigest()
		else:
			return hashlib.sha256(FileHandle.read()).hexdigest()


def DeleteDuplicateFiles(DirectoryPath):
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

def WriteOutputLog(LogDir, FileOutput):
	try:
		if not os.path.exists(LogDir):
			os.makedirs(LogDir)

		Header = "-" * 20 + "\nProcesses Log:"+ time.ctime() + "\n"
		LogTime = time.ctime()
		LogFileName = datetime.datetime.now().strftime("ProcessMonitorLog_%d-%m-%Y_%H-%M-%S.txt") 
		LogFileAbsPath = os.path.join(LogDir, LogFileName)
		with open(LogFileAbsPath, "w", encoding = "utf-8") as fp:
			fp.write(Header)
			if isinstance(FileOutput, list):
				fp.writelines(FileOutput)
			else:
				fp.write(FileOutput)
		return LogFileAbsPath, LogTime
	except ValueError:
		if LogFileAbsPath:
			with open(LogFileAbsPath, "a") as fp:
				fp.write("Failed to send mail: Invalid datatype of input.")
	except Exception as ex:
		if LogFileAbsPath:
			with open(LogFileAbsPath, "a") as fp:
				fp.write("Failed to send mail: {}".format(str(ex)))	

# for text files
# Receivers - list of str (email addrs), Sender - str (email addr)
def SendLogMail(Sender, Receivers, Subject, Message, AppPwd, Files = None, Host = "smtp.gmail.com", Port = 465):
	try:
		msg = MIMEMultipart()
		msg["From"] = Header(Sender)
		# msg["To"] = Header(Receivers)
		msg['To'] = Header(", ".join(Receivers)) # multiple recipients
		msg["Subject"] = Header(Subject)
		msg.attach(MIMEText(Message, "html", "utf-8"))

		if Files:
			for File in Files:
				AttachmentName = os.path.basename(File)
				Attachment = MIMEText(open(File, "rb").read(), "base64", "utf-8")
				Attachment["Content-Type"] = "application/octet-stream"
				Attachment["Content-Disposition"] = "attachment; filename=" + AttachmentName
				msg.attach(Attachment)

		Server = smtplib.SMTP_SSL(Host, Port)
		Server.login(Sender, AppPwd)
		Server.sendmail(Sender, Receivers, msg.as_string())
		Server.quit()
	except ValueError:
		print("Failed to write log file: Invalid datatype of input.")
	except Exception as ex:
		print("Failed to write log file: ", str(ex))
	# print("Sent Email Successfully !!")

def DuplicateFilesRemovalTasks(CommandLineArgs):
	# validation & get deleted duplicate files - argv[1]
	FileOutput = None
	if len(CommandLineArgs) != 3:
		FileOutput = "Error: Invalid no. of arguments. Sample Correct Usage: 'DuplicateFilesRemoval.py Demo 50 email_id_1,email_id_2'. 50 is time interval in minutes for scheduling. For multiple email ids, make sure to add them comma (without space) separated."
	else:
		FileOutput = DeleteDuplicateFiles(CommandLineArgs[1])
	
	# write output in log file
	if FileOutput:
		LogFilePath, LogTimeForMail = WriteOutputLog("Shruti", FileOutput)
		

	# mail the log file - argv[3]
	if LogFilePath:
		SendLogMail("shruti.p109@gmail.com", CommandLineArgs[3].split(","), "Process Monitor Log " + LogTimeForMail , "Hello, This is a test mail.<br>Please find Process Monitor Log generated on <b>" + LogTimeForMail + "</b>.\n", "tzrioxmszzgauhxq", [LogFilePath])
		

def main():
	if argv[1] == "-h" or argv[1] == "-H":
		print("This script is used to delete duplicate files in given directory & mail the log file to given mail id at given interval.")
		exit()

	if argv[1] == "-u" or argv[1] == "-U":
		print("Usage : application_name directory_path schedule_time_in_minutes email_id")
		exit()

	try:
		schedule.every(int(argv[2])).minutes.do(DuplicateFilesRemovalTasks, CommandLineArgs = argv)
	except ValueError:
		WriteOutputLog("Shruti", "Failed to execute task: Invalid datatype of input.")

	DuplicateFilesRemovalTasks(argv)

if __name__ == "__main__":
	main()