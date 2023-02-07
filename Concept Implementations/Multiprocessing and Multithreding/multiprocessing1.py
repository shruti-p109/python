import time
import multiprocessing
import os

# dont run name file mulitiprocessing (same sa in-built python module name)

# display even nos until no
def DisplayEven(No):
	print("DisplayEven Process ID of worker process is {} for input {}".format(os.getpid(), No))
	print("DisplayEven Parent Process ID of worker process is {} for input {}".format(os.getppid(), No)) # same for both processes
	for i in range(No+1):
		if i % 2 == 0:
			print("Even Number:", i)

# display odd nos until no
def DisplayOdd(No):
	print("DisplayOdd Process ID of worker process is {} for input {}".format(os.getpid(), No))
	print("DisplayOdd Parent Process ID of worker process is {} for input {}".format(os.getppid(), No))
	for i in range(No+1):
		if i % 2 != 0:
			print("Odd Number:", i)

def main():
	print("Demonstration of Paralle Programming using multiple processes:")
	Number = 200
	# processes handles - processes will not start until you explicitly tell to start
	# To create a tuple with only one item, you have add a comma after the item, otherwise Python will not recognize the variable as a tuple.
	p1 = multiprocessing.Process(target = DisplayEven, args = (Number,))
	p2 = multiprocessing.Process(target = DisplayOdd, args = (Number,))

	# both will execute parallerly
	p1.start() # start() - gets added to queue (scheduled)
	p2.start()

	# when a scheduled proess will start executing (waiting time) - depends on pvm scheduler

	# joins processes back to parent process (after they are finished)
	p1.join() # join() - stop, dont go forward until execution of p1 finishes - tells main process to stop/wait until p1 execution finishes
	p2.join()

	print("End of main") # wihtout join - this may execute before p1 or p2 finishes 

if __name__ == "__main__":
	StartTime = time.time()
	StartProcessTime = time.process_time()
	main()
	EndProcessTime = time.process_time()
	EndTime = time.time()
	print("Execution Time:", EndTime - StartTime) # execution time of whole application
	print("Actual Process Execution Time:", EndProcessTime - StartProcessTime) # only cpu time - execution time of process