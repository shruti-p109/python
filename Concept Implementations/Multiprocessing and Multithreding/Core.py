# multitasking
# Author : Shruti Pimparkars

import multiprocessing
import os # for me - windows specific os module, for mac laptop - mac os specific module

def main():
	# control flow - prg -> pvm -> kernel (as pvm does not have this os related info)
	print("Number of cores:",multiprocessing.cpu_count())
	print("PID of current process:",os.getpid())
	print("PPID of current process:",os.getppid()) # if run from cmd - its PID of cmd - stays same if prg run again & again from same cmd window
	# check from task manager - checked - you can see PID of each process in Details tab
if __name__ == "__main__":
	main()