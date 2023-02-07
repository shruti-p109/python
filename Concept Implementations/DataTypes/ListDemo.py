# Demo for list sequence datatype
# Author : Shruti Pimparkar

def main():
	print("Demo of list sequence datatype")

	# data - heterogeneous - allowed
	# ordered - yes
	# indexed - yes - 0 1 2
	# mutable - yes - written by pencil | immutable - written by pen | mutable - not changing 11 to 12, means removing 11 & adding 12 
		# - see mutability as a whole
	# duplicates - allowed

	# of data is ordered - then indexed,if not ordered - not indexed as index is type of ordering the data,can't do it if data is unordered

	data = [11, 90.80, True, "Hello", 11]

	print(data)
	print(type(data))
	print("Duplicates:", data)
	print("Heterogeneous", data)
	print("Data at index 2", data[2])

	print("Mutable")
	data.append(40) # inserts at end - append func only for ordered data - end, first has meaning only for ordered data
	print("Data after append", data)
	data.pop() # removed from end
	print("Data after pop", data)
	# insert - adds at given index - after insert all elements shift by 1 index - no overwrite

	# many methods like this - for each datatype - you need not know all these in-built methods - but - 
	# you should be able to write logic for these in-built methods if needed - if you can google - use it for finding & usage of these methods

if __name__ == "__main__":
	main()