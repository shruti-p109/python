import psutil
from sys import *
import os
import datetime
import time

def LogProcessInfo(LogDir = "Logs"):
	if not os.path.exists(LogDir):
		try:
			print('mkdirs')
			# os.mkdirs(LogDir)
			os.makedirs(LogDir)
		except:
			pass

	Separator = "-" * 20
	LogFileAbsPath = os.path.join(LogDir, datetime.datetime.now().strftime("ProcessMonitorLog_%d-%m-%Y_%H-%M-%S.log"))
	f = open(LogFileAbsPath, "w")
	f.write(Separator + "\n")
	f.write("Process Logger:"+ time.ctime() + "\n")

	ProcessList = list()
		# print(type(psutil.process_iter())) # <class 'generator'>
	for Process in psutil.process_iter():
		# print(type(process)) # <class 'psutil.Process'>
		# print(help(psutil.Process))
		try:
			ProcessInfo = Process.as_dict(attrs = ["pid", "name", "username"]) # returns dict containing asked attributes
			ProcessInfo["vms"] = Process.memory_info().vms / (1024 * 1024)
			# vms / rss returned will be in bytes, we converted it into MB
			# rss is the Resident Set Size, which is the actual physical memory the process is using
			# vms is the Virtual Memory Size which is the virtual memory that process is using
			ProcessList.append(ProcessInfo)
		except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
			pass
		# An orphan process is formed when it's parent dies while the process continues to execute, while zombie process is a process which has terminated but it's entry is there in the process table.

	for element in ProcessList:
		f.write("%s\n"%element)

	f.close()


def main():
	print("Process Monitor with memory usage:")

	if len(argv) != 2:
		print("Error: Invalid number of arguments.")
		exit()

	if argv[1] == "-h" or argv[1] == "-H":
		print("This Script is used to log information of running processes on the system.")
		exit()

	if argv[1] == "-u" or argv[1] == "-U":
		print("Usage: application_name log_directory_absolute_path")
		exit()

	try:
		LogProcessInfo(argv[1])
	except ValueError:
		print("Error: Invalid datatype of input.")
	except Exception as ex:
		print("Error: ", str(ex))

if __name__ == "__main__":
	main()