import time
import threading
import os

# display even nos until no
def DisplayEven(No):
	# get_ident - returns python id of thread
	# get_native_id - returns os id of thread
	print("DisplayEven Thread ID of worker thread is {} for input {}".format(threading.get_native_id(), No))
	print("DisplayEven Process ID of worker process is {} for input {}".format(os.getpid(), No)) # same for both threads
	print("DisplayEven Parent Process ID of worker process is {} for input {}".format(os.getppid(), No)) # same for both threads
	for i in range(No+1):
		if i % 2 == 0:
			print("Even Number:", i)

# display odd nos until no
def DisplayOdd(No):
	print("DisplayOdd Thread ID of worker thread is {} for input {}".format(threading.get_native_id(), No))
	print("DisplayOdd Process ID of worker process is {} for input {}".format(os.getpid(), No))
	print("DisplayOdd Parent Process ID of worker process is {} for input {}".format(os.getppid(), No))
	for i in range(No+1):
		if i % 2 != 0:
			print("Odd Number:", i)

def main():
	print("Demonstration of Paralle Programming using multiple threads:")
	Number = 200
	# thread handles - threads will not start until you explicitly tell to start
	t1 = threading.Thread(target = DisplayEven, args = (Number,)) # args - tuple, comma - search
	t2 = threading.Thread(target = DisplayOdd, args = (Number,))

	# multithreading, multiprocessing - not that easy if target func is returning something - soln - bad prg practice - store return value
	# in global variable

	# both will execute parallerly
	t1.start() # start() - gets added to queue (scheduled)
	t2.start()

	# when a scheduled proess will start executing (waiting time) - depends on pvm scheduler

	# joins threads back to parent process (after they are finished)
	t1.join() # join() - stop, dont go forward until execution of t1 finishes - tells main thread to stop/wait until t1 execution finishes
	t2.join()

	print("End of main")  # wihtout join - this may execute before t1 or t2 finishes 

if __name__ == "__main__":
	StartTime = time.time()
	StartProcessTime = time.process_time()
	main()
	EndProcessTime = time.process_time()
	EndTime = time.time()
	print("Execution Time:", EndTime - StartTime) # execution time of whole application
	print("Actual Process Execution Time:", EndProcessTime - StartProcessTime) # only cpu time - execution time of process