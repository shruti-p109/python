# def Demo():
# 	print("Inside Demo function")

def Hello():
	print("Inside Hello function")
	# Inner Function (helper function) - only in python 
	def Demo():
		print("Inside Demo function")
	Demo()

Hello()
# Demo() # NameError: name 'Demo' is not defined
# Inner Function can not be called from outside the parent function - Abstraction
