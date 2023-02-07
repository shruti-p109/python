# Demo for set sequence datatype
# Author : Shruti Pimparkar

def main():
	print("Demo of Set sequence datatype")

	# data - heterogeneous - allowed
	# ordered - No
	# indexed - No
	# mutable - yes, immutable - no
	# duplicates - not 	allowed

	data = {"fsdfds", 11, 90.80, True, "Hello", 11} # no error - but will remove duplicate - {True, 90.8, 11, 'Hello'}

	print(data) # data un-ordered, different order than you added
	print(type(data))
	print("Duplicates removed:", data) # no error - but will remove duplicate - {True, 90.8, 11, 'Hello'}
	print("Heterogeneous", data)
	# print("Data at index 2", data[2]) # TypeError: 'set' object is not subscriptable -> set is not indexed

	# print("Mutable")
	# data.append(40) # error as set data is not ordered, append at end - has no meaning
	# print("Data after append", data)
	data.pop()
	print("Data after pop", data) # dont pay attention to from where it removed - no meaning - unordered

	data.add("shruti")
	print("Data after add", data) # dont pay attention to from where it added - no meaning - unordered

	# data.remove("fsdfdsssssss") # KeyError: 'fsdfdsssssss' - exception - use this if you want to throw exception if value is non-existent
	data.discard("fsdfdsssssss") # will remove if its there, if its not there - no error - which to use - dep on req
	print("Data after discard fsdfdsssssss", data)
	data.remove("fsdfds")
	print("Data after remove fsdfds", data)

if __name__ == "__main__":
	main()