# accept size & integers from user and add them in list

def main():
	Arr = list() # create empty list - syntax dependent on version - object of class list
	# Arr = [] # alternate syntax, 1st one preferred

	print("Enter no of elements:")

	size = int(input())

	for i in range(0,size):
		print("Enter integer element:")
		no = int(input())
		Arr.append(no) # or Arr.insert(i,no)
		print(Arr)

if __name__ == "__main__":
	main()