# multitasking
# Author : Shruti Pimparkars

# platform dependent - if PID of each input -  same - os did not feel like creating separate processes
# ran on multiple cores parallely - square for each input
# multi - core

import os
import multiprocessing

def Square(No):
	print("Process ID of worker process is {} for input {}".format(os.getpid(), No))
	print("Parent Process ID of worker process is {} for input {}".format(os.getppid(), No))
	return No * No

def main():
	print("Process ID of application is", os.getpid())
	Data = [1, 2, 3, 4, 5]
	Result = list()

	# serial
	# for value in Data:
	# 	Result.append(Square(value))

	# parallel
	pobj = multiprocessing.Pool() # pool that stores multiple processes
	# a process for each input/function call - for above list - 5 calls, 5 prpcesses with 1 common parent process - ppis will be same for all 5
	# map - will call Square for each input in 'Data' list 
	Result = pobj.map(Square, Data)
	print("Result after operation:", Result)

if __name__ == "__main__":
	main()