# Author : 				Shruti Pimparkar
# Problem Statement : 	Multithreading but scheduled serially

import threading

# Display 1 to 50
def Display():
	for i in range(1,51):
		print(i)

# Display 50 to 1
def DisplayRev():
	for i in range(50,0,-1):
		print(i)

def main():
	Thread1 = threading.Thread(target = Display)
	Thread2 = threading.Thread(target = DisplayRev)

	Thread1.start() # schedule thread1

	Thread1.join() # wait until thread1 finishes

	Thread2.start() # schedule thread2

	Thread2.join()

	print("End of main")

if __name__ == "__main__":
	main()

