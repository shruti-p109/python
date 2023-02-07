# recursion
# argument 4, print 4 3 2 1

# 1st write while loop
def Display(No):
	while No > 0:
		print(No, end = " ")
		No -= 1

Display(4)

print()
# converting iteration to recursion
# while -> if

#  displays while going forward, only decrements while backtracking
# tail recursion
def DisplayR(No):
	if No > 0:
		print(No, end = " ")
		No -= 1
		DisplayR(No)
		
DisplayR(4)

print()
# Edit above func so that it will display 1 2 3 4

# displays while backtracking
# head recursion
def DisplayRRev(No):
	if No > 1:
		No -= 1
		DisplayRRev(No)
		print(No, end = " ")
		
DisplayRRev(4)

# head recursion - recursive call not at end
# tail recursion - last line of func - recursive call