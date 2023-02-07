# recursion
# removed counter, handled logic by modified argument
def Display(No): # Display(4) Display(3) Display(2) Display(1) | Display(0) - will not go inside if - no recursive call
	if No > 0: 
		print("Hello")
		No -= 1 
		Display(No)

Display(4)