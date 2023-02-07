# Author:	Shruti Pimparkar
# Problem Statement: Task Scheduler - Display "Hello World!" on console every minute

import schedule
import time
import datetime

def TaskPerMinute():
	print("Inside TaskPerMinute, current time is", datetime.datetime.now())

def TaskPerHour():
	print("Inside TaskPerHour, current time is", datetime.datetime.now())

def TaskOnSaturday():
	print("Inside TaskOnSaturday, current time is", datetime.datetime.now())

def main():
	print("Inside main")
	print("Current time is",datetime.datetime.now())

	schedule.every(1).minutes.do(TaskPerMinute)
	schedule.every(1).hour.do(TaskPerHour)
	schedule.every().saturday.at("18:00").do(TaskOnSaturday)

	while(True):
		schedule.run_pending() 
		time.sleep(1) 


if __name__ == "__main__":
	main()