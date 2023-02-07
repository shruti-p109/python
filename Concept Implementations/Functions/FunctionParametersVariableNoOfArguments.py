# Function Argument Types
# Author : Shruti Pimparkar

def Add(*Nos):
	# print(type(Nos)) # tuple because its immutable
	print("No. of arguments :",len(Nos))
	Sum = 0

	# for No in Nos:
	# 	Sum += No
	
	for i in range(len(Nos)):
		Sum += Nos[i]

	return Sum

def main():
	Ans = Add(10, 20, 30, 5 , 4)
	print("Addition is :", Ans)

# starter - from where execution starts
if 	__name__ == "__main__":
	main()
