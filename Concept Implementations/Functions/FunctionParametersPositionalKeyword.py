# Function Argument Types
# Author : Shruti Pimparkar

# Posiional / Position / Required Arguments - Mandatory & in proper sequence / position | Keyword arguments - see call
def Add1(No1, No2):
	print("Demo1, value of No1 :", No1)
	print("Demo1, value of No2 :", No2)
	return No1 + No2

def main():
	Ans = 0 # sets datatype of Ans, also initializes it
	Ans = Add1(10, 10)
	print("Add1 positional call return value :", Ans)
	# keyword args call - you need to know the names of arguments for this kind of call - you should create proper doc in this case
	# if you dont know sequence of arguments - go for keyword call
	Ans1 = Add1(No2=23, No1=3)
	print("Add1 keyword call return value :", Ans1)

# starter - from where execution starts
if 	__name__ == "__main__":
	main()

