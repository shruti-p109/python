import psutil
# Generator functions allow you to declare a function that behaves like an iterator, i.e. it can be used in a for loop.

def GetProcessList():
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
	return ProcessList

def main():
	print("Process Monitor with memory usage:")
	for EachProc in GetProcessList():
		print(EachProc)

if __name__ == "__main__":
	main()