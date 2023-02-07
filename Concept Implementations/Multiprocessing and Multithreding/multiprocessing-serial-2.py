import time

# display even nos until no
def DisplayEven(No):
	for i in range(No+1):
		if i % 2 == 0:
			print("Even Number:", i)

# display odd nos until no
def DisplayOdd(No):
	for i in range(No+1):
		if i % 2 != 0:
			print("Odd Number:", i)

def main():
	print("Demonstration of Serial Programming:")
	StartTime = time.time()
	StartProcessTime = time.process_time()
	DisplayEven(2000)
	DisplayOdd(2000)
	EndProcessTime = time.process_time()
	EndTime = time.time()
	print("Execution Time:", EndTime - StartTime) # execution time of whole application
	print("Actual Process Execution Time:", EndProcessTime - StartProcessTime) # only cpu time - execution time of process


if __name__ == "__main__":
	main()