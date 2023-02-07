# passing Demo function as argument of Hello function & calling it
def Demo():
	print("Inside Demo function")

def Fun():
	print("Inside Fun function")

def Square(param):
	print("Inside Gun function. parameter is", param)
	return param * param

# naked prototyping
# func_name argument - like reference
def Hello(func_name): # condition - func_name can not accept any argument
	print("Inside Hello function")
	func_name()

def Hello1(func_name, func_arg):
	print("Inside Hello1 function")
	return func_name(func_arg)

Hello(Demo) # condition - Demo func can not accept any argument
Hello(Fun)
# Hello(11)

# print("Return value of Square function call is", Hello1(func_name = Square, 11)) # SyntaxError: positional argument follows keyword argument
print("Return value of Square function call is", Hello1(func_name = Square, func_arg = 11))