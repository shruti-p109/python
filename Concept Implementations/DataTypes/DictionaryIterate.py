# Iterate dictionary
# Author : Shruti Pimparkar

def main():
	print("Iterate dictionary")

	batches = {"PPA": 18000, "LB": 16700, "Python":16500, "Angular": 15000, "PPA": 17500} # value of PPA key will get overwritten as 17500

	print("Data traversal using for, keys")
	for x in batches:
		print(x) # keys

	print("=====================")

	# faster than .get(key) as later one is function call
	print("Data traversal using for, values using keys")
	for x in batches:
		print(x, batches[x]) # values by keys

	print("=====================")

	print("Data traversal using for, values using keys using .get(key)")
	for x in batches:
		print(x, batches.get(x)) # values by keys using get()

	keyBatches = batches.keys()
	print(keyBatches) # dict_keys(['PPA', 'LB', 'Python', 'Angular']) -> square brackets - list
	print(type(keyBatches)) # <class 'dict_keys'> - internally list

	valueBatches = batches.values()
	print(valueBatches) # dict_values([18000, 16700, 16500, 15000]) -> square brackets - list
	print(type(valueBatches)) # <class 'dict_values'>

	print("=====================")

	# traverse both keyBatches & valueBatches at same time to get pairs - order is same - correct pairing
	for i in range(len(batches)):
		# print(keyBatches[i], valueBatches[i]) # TypeError: 'dict_keys' object is not subscriptable
		# explicitly convert dict_keys into list then can access by index like above
		print(list(keyBatches)[i], list(valueBatches)[i]) # TypeError: 'dict_keys' object is not subscriptable

if __name__ == "__main__":
	main()