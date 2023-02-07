# Author:	Shruti Pimparkar
# Problem Statement: Task Scheduler - Stop application after task is executed certain times

import schedule
import time
import datetime
import sys

TaskExecutionCounter = 0
# or write schedule terminator func & schedule it after 2 mins

def TaskPerMinute():
	global TaskExecutionCounter
	if TaskExecutionCounter == 2:
		print("Task executed 2 times, exiting")
		sys.exit()
	print("Inside TaskPerMinute, current time is", datetime.datetime.now())
	TaskExecutionCounter += 1

def main():
	print("Inside main")
	print("Current time is",datetime.datetime.now())

	schedule.every(1).minutes.do(TaskPerMinute)

	while(True):
		schedule.run_pending() 
		time.sleep(1) 


if __name__ == "__main__":
	main()