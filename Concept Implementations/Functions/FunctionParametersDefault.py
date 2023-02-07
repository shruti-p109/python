# Function Argument Types
# Author : Shruti Pimparkar

def CircleArea(Radius, PI):
	return PI * Radius * Radius

# Default Arguments - need to mention while defining the function
def CircleAreaDefault(Radius, PI=3.14):
	return PI * Radius * Radius

def main():
	RValue = 10.5
	PIValue = 3.14
	# positional
	Ans = CircleArea(RValue, PIValue) # manually cal value = 346.185
	print("Area of circle is :", Ans)

	# keyword
	Ans1 = CircleArea(PI=3.14, Radius=10.5)
	print("Area of circle is by keyword arg call :", Ans1)

	# default
	Ans2 = CircleAreaDefault(10.5)
	print("Area of circle is by calling default arg funciton :", Ans2)

	# keyword + default
	Ans3 = CircleAreaDefault(Radius=10.5)
	print("Area of circle is keyword + default call :", Ans3)

	# keyword + default overwritten
	Ans4 = CircleAreaDefault(PI=7.10, Radius=10.5) # manually cal value = 782.775
	print("Area of circle is keyword + default overwritten call :", Ans4)

	# default overwritten
	Ans5 = CircleAreaDefault(10.5,7.10)
	print("Area of circle is default overwritten call :", Ans5)

	# error - SyntaxError: positional argument follows keyword argument
	# Ans6 = CircleAreaDefault(Radius=10.5,7.10)
	# print("test :", Ans6)

	# allowed
	Ans6 = CircleAreaDefault(10.5,PI=7.10)
	print("test1 :", Ans6)

# starter - from where execution starts
if 	__name__ == "__main__":
	main()

