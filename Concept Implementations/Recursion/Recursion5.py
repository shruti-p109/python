def AddNos(No):
	Sum = 0
	while No > 0:
		Sum += No
		No -= 1
	return Sum

print(AddNos(4))

# problem - function is returning something, instead of just printing

def AddNosR(No):
	if No == 0:
		return 0
	else:
		return No + AddNosR(No-1)

print(AddNosR(4))

# factorial
def FactorialR(No):
	if No == 0:
		return 1
	else:
		return No * AddNosR(No-1)

print(FactorialR(4))