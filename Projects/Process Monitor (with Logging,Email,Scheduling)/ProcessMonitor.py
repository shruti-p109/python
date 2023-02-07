import psutil
# Generator functions allow you to declare a function that behaves like an iterator, i.e. it can be used in a for loop.

def GetProcessList():
	ProcessList = list()
		# print(type(psutil.process_iter())) # <class 'generator'>
	for Process in psutil.process_iter():
		# print(type(process)) # <class 'psutil.Process'>
		# print(help(psutil.Process))
		try:
			ProcessInfo = Process.as_dict(attrs = ["pid", "name", "username"])
			ProcessList.append(ProcessInfo)
		# AccessDenied - while accessing os process, NoSuchProcess - process got killed when you got its info but when
		# accessing later on it was terminated, ZombieProcess - process is terminated but its entry is still in process table
		except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
			pass
		# An orphan process is formed when it's parent dies while the process continues to execute, while zombie process is a process which has terminated but it's entry is there in the process table.
	return ProcessList

def main():
	print("Process Monitor:")
	for EachProc in GetProcessList():
		print(EachProc)

if __name__ == "__main__":
	main()