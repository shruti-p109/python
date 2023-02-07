# abstracted function we want to use but with our modifications/addition/change in return value/change in arguments
# you can decorate in-built functions as well - try
# name, parameters, types pf params, return value, what is the function doing - doc / info required func you want to decorate
def Subtraction(No1, No2): # function which we dont have access to modify, modification to add - always return +ve subtraction
	return No1 - No2

# used as design pattern in companies - Decorator pattern
# A decorator is a programming design pattern where you wrap something in something else to change some aspect of the original's behavior.
# not python specific concept
# decorator - returns you new modified function which you can call (which have modification + internally calls original)
# userdefined decorator - @ symbol not required
# oops decorators - in-built decorators
def DecoratedFunction(FunctionName):
	def InnerFunction(A, B):
		if A < B:
			A, B = B, A # multiassignment # swap
		return FunctionName(A, B) # calling FunctionName with arguments given to InnerFunction & returning its return value
	return InnerFunction

def main():
	# input function takes 1st argument as prompt/string to print (w/o newline) before taking entered input from user
	Value1 = int(input("Enter first number:"))
	Value2 = int(input("Enter second number:"))

	NewFunction = DecoratedFunction(Subtraction) # NewFunction - id of InnerFunction
	# NewFunction - Subtraction logic + our modification ( but w/o touching subtraction definition)
	# below line - calling InnerFunction
	print("Subtraction is:",NewFunction(Value1, Value2)) # even if Value1 < Value2, Subtraction should come as +ve
	# due to swapping in DecoratedFunction before Subtraction (FunctionName) function call

	# from above, purpose of decorated function - Subtraction - func defined by some other developer, you only have its .pyc file, you
	# are not allowed modify this function, so we are 'decorating' it before calling it to integrate our desirable modifications 
	# in logic of Subtraction function

if __name__ == "__main__":
	main()

# in c - funcion name, array name - contains its address