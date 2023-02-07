# Function types
# Author : Shruti Pimparkar

# Function which accepts nothing and returns nothing
def Demo1():
	print("Inside Demo1")

# Function accepts one argument and returns nothing
def Demo2(No):
	print("Inside Demo2 with argument :", No)

# Function which accepts one argument and returns one value
def Demo3(No):
	print("Inside Demo3 with argument :", No)
	return No + 2

# Functions accepts two arguments and returns 1 value
def Demo4(No1, No2):
	print("Inside Demo4 with arguments :", No1, No2)
	Add = No1 + No2
	return Add

# Functions which return nothing - called - service providers

# Function which accepts two arguments and returns two values - only in python
def Demo5(No1, No2):
	print("Inside Demo5 with arguments :", No1, No2)
	Add = No1 + No2
	Sub = No1 - No2
	return Add, Sub

def main():
	Demo1()
	Demo2("shruti")
	Ans = Demo3(11)
	print("Return value of Demo3 is :", Ans)
	Ans1 = Demo4(10, 11)
	print("Return value of Demo4 is :", Ans1)
	Ans2, Ans3 = Demo5(10, 11) # if you catch it in only 1 variale, you will get tuple of (Add, Sub)
	print("First return value of Demo5 is :", Ans2)
	print("Second return value of Demo5 is :", Ans3)

# starter - from where execution starts
if 	__name__ == "__main__":
	main()
