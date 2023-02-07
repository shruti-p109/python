# Author:	Shruti Pimparkar
# Problem Statement: File IO - Read & Close

from os.path import exists

def ReadFile(FileName):
	if exists(FileName):
		fd = open(FileName, "w")
		# print(type(fd.read())) # <class 'str'>
		print("Data in given file is:")
		print(fd.read())
		fd.close() # close opened file - gets closed when prg terminates but its good practice to release all resources

	else:
		print("File does not exist.")


def main():
	print("Enter the file name to open for reading:")
	Name = input()

	ReadFile(Name)

if __name__ == "__main__":
	main()

# The default is reading in text mode. In this mode, we get strings when reading from the file.
# On the other hand, binary mode returns bytes and this is the mode to be used when dealing with non-text files like images or executable files.

# f.readline() - reads 1st line
# f.readline() - reads next line
# f.readlines() - returns list of lines
# f.read(4) - first 4 data
# f.read(4) - next 4 data
# f.tell() - get the current file position
# f.seek(0) - move cursor to 0th (offset) position
# for line in f: - read line by line
# 	print(line, end = '')
