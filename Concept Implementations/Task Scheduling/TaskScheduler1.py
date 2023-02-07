# Author:	Shruti Pimparkar
# Problem Statement: Task Scheduler - Display "Hello World!" on console every minute

import schedule
import time
import datetime

def Fun():
	print("Hello World!, time is",datetime.datetime.now())

def main():
	print("Inside main")
	print("Current time is",datetime.datetime.now())

	schedule.every(1).minutes.do(Fun) # depends on your system clock
	# after scheduling you need to stand & wait otherwise schedule will be discarded - to run cont - loop

	while(True):
		schedule.run_pending() # run task if pending, this is compulsory - if before starting of next iteration - task got skipped - you need to check if anything is pending
		time.sleep(1) # sleep for 1 sec # reason - if not slept its a task for os/microprocesser, can increase sleep time

	# above execution may be delayed by 1 sec - slept at last sec of 60 sec completion - 61st sec - awake - ran pending task - 1 sec delay

	# if you close command prompt - killed parent process - program will be killed as well - solution - add it to daemon
	# or control c - abort - keyboardInterrupt

	# if you want to execut at 8.1 but task scheduled at 8 is taking 1.5 minutes - delay by 0.5 minutes

if __name__ == "__main__":
	main()