# Author:	Shruti Pimparkar
# Problem Statement: File IO - Write

from os.path import exists

def WriteFile(FileName):
	# here we are wrting if it exists, if not doing nothing
	if exists(FileName):
		print("Enter data to write in file:")
		Data = input()
		# append at end of file to avoid data loss if present
		fd = open(FileName, "a")
		fd.write("\n" + Data)
		print("Done")

	else:
		print("File does not exist.")


def main():
	print("Enter the file name to open for writing:")
	Name = input()

	WriteFile(Name)

if __name__ == "__main__":
	main()
