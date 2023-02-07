# Demo for sequence datatypes
# Author : Shruti Pimparkar

def main():
	print("Demo of sequence datatypes")

	lData = [10, 20, 30, 40] # list []
	tData = (10, 20, 30, 40) # tuple ()
	sData = {10, 20, 30, 25} # set {}
	dData = {"c":400, "c++":450, "java":200, "python":890} # dictionary {} - like hashtable / hashmap - like json - key:value pair 
	# - give key take value

	print(lData)
	print(type(lData))
	print(tData)
	print(type(tData))
	print(sData) # output - eg. - {25, 10, 20, 30} - not ordered - elements not necessarily placed in memory as added (orderwise)
	print(type(sData))
	print(dData) # python > 3.7 & < 3.7 - difference
	print(type(dData))

if __name__ == "__main__":
	main()