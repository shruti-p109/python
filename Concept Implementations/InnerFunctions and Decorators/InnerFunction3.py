# returning func from another function
def Outer():
	print("Inside Outer")
	def Inner():
		print("Inside Inner")
	print(id(Inner))
	# return id of inner func
	return Inner # returning inner function itself, this is why return value of Outer will be callable

InnerOfOuter = Outer()
print(type(InnerOfOuter)) # <class 'function'>
print(id(InnerOfOuter)) # will be same as output of line 6
InnerOfOuter() # calling inner func of outer funcs, we can inner func because outer is returning it - breaking of abstraction - outer is allowing it