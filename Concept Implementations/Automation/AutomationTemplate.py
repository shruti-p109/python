from sys import *

def ScriptTask(No):
	if No % 2 == 0:
		print("Even")
	else:
		print("Odd")

def main():
	print("--------- Shruti Pimparkar ----------")
	print("Automation script started with", argv[0])

	if len(argv) != 2:
		print("Error :Insufficient arguments. Use -h for help and -u for usage of script")
		print("Use -h for help and -u for usage of script")
		exit()

	if argv[1] == "-h" or argv[1] == "-H":
		print("This script is used to perform ____")
		exit()

	elif argv[1] == "-u" or argv[1] == "-U":
		print("Usage : Provide ____ number of arguments as")
		print("First Argument as: _____")
		print("Second Argument as: _____")

	else:
		# print("Error: There is no {} flag for this script".format(argv[1]))
		# exit()
		try:
			ScriptTask(int(argv[1]))
		except Exception:
			print("Error: Wrong Arguments.")
			print("Use -h for help and -u for usage of script")

if __name__ == "__main__":
	main()