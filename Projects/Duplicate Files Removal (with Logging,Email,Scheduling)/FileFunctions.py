import time
import hashlib
import os

def GenerateChecksum(File, BytesToRead = None):
	# with syntax - takes care of clean-up such as closing the file
	with open(File, mode = "rb") as FileHandle:
		if BytesToRead:
			return hashlib.sha256(FileHandle.read(int(BytesToRead))).hexdigest()
		else:
			return hashlib.sha256(FileHandle.read()).hexdigest()

def WriteOutputLog(FileOutput, LogFileName, LogDir = "Logs"):
	try:
		if not os.path.exists(LogDir):
			os.makedirs(LogDir)

		LogTime = time.ctime() 
		LogFileAbsPath = os.path.join(LogDir, LogFileName)
		with open(LogFileAbsPath, "a", encoding = "utf-8") as fp:
			if isinstance(FileOutput, list):
				fp.writelines(FileOutput)
			else:
				fp.write(FileOutput)
		return LogFileAbsPath, LogTime
	except ValueError:
		if LogFileAbsPath:
			with open(LogFileAbsPath, "a") as fp:
				fp.write("Failed writing log file: Invalid datatype of input.")
	except Exception as ex:
		if LogFileAbsPath:
			with open(LogFileAbsPath, "a") as fp:
				fp.write("Failed writing log file: {}".format(str(ex)))	