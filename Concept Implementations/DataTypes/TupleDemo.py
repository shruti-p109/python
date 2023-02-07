# Demo for tuple sequence datatype
# Author : Shruti Pimparkar

def main():
	print("Demo of tuple sequence datatype")

	# data - heterogeneous - allowed
	# ordered - yes
	# indexed - yes
	# mutable - no, immutable - yes
	# duplicates - allowed

	data = (11, 90.80, True, "Hello", 11)

	print(data)
	print(type(data))
	print("Duplicates:", data)
	print("Heterogeneous", data)
	print("Data at index 2", data[2])

	# print("Mutable") - not mutable
	# data.append(40) # will give error - no append method available
	# print("Data after append", data)
	# data.pop() # will give error - no pop method
	# print("Data after pop", data)

	# you can not insert or remove after creating the tuple - like - const arr - not drawback - its property - use it accordinly
	# tuple - fast iteration as stored read only memory
	# if someone says yes i can add element in tuple - not directly - convert to list - add - convert back to tuple - technically can not 
	# add to tuple
	# non modifible data - store in tuple

	# mutability - tuple's not tuple's data's 

if __name__ == "__main__":
	main()