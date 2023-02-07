# Author:	Shruti Pimparkar
# Problem Statement: File IO - Creation

from os.path import exists

def CreateFile(FileName):
	# open() - creates new file as well as opens existing file
	# fd = open(FileName) # FileNotFoundError: [Errno 2] No such file or directory: 'shruti', if exists no error, no change in file
	# fd = open(FileName, "w") # create file if its not there, if its there it will be removed & new one with the same name will be created. Also file will be created in current directory

	# we want to check & create file if it doesnt exists, if it does dont do anything
	if exists(FileName):
		print("File exists")
	else:
		print("File does not exist.Creating it..")
		fd = open(FileName, "w")
		print("Done")


def main():
	print("Enter the file name to create:")
	Name = input() # give extension as well

	CreateFile(Name)

if __name__ == "__main__":
	main()
