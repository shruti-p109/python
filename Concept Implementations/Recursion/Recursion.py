# display function to display (parameter) times hello on screen

# to convert iteration to recurion - while loop is best to understand
def Display(No):
	Count = 0
	while Count < No: # remove while -> if
		print("Hello")
		Count += 1 # at end of if call same func

Display(4)