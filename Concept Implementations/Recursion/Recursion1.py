# display function to display (parameter) times hello on screen
# in python - pvm itself aborts prg if its not stopping
# in c - prg will keep going for infinite loop, until stack overflow
# to convert iteration to recurion - while loop is best to understand
def Display(No):
	Count = 0
	if Count < No: # remove while -> if
		print("Hello")
		Count += 1 # at end of if call same func
		Display(No) # RecursionError: maximum recursion depth exceeded while calling a Python object - stack overflow

Display(4)