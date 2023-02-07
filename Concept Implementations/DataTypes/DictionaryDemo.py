# Demo for dictionary sequence datatype
# Author : Shruti Pimparkar

def main():
	print("Demo of dictionary sequence datatype")

	# data - heterogeneous - allowed
	# ordered - Yes
	# indexed - No (not integral but by key yes)
	# mutable - yes
	# duplicates keys - not allowed
	# duplicate values - allowed

	programming = {"c":"Ritchie", "c++":"Stroustroupe", "java":"Ghosling", "python":"Rossum"}
	batches = {"PPA": 18000, "LB": 16700, "Python":16500, "Angular": 15000}

	print("Data of dictionary batches:", batches)
	print("Data of dictionary programming:", programming)
	print("Datatype is:", type(batches))
	print("Length of dictionary batches:", len(batches))

	print()

	print("Value of PPA in batches:", batches["PPA"])

	# add a pair
	batches["Unix OS"] = 12300

	print("Data of dictionary batches after adding a pair:", batches)

if __name__ == "__main__":
	main()