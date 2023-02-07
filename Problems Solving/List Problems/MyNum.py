def IsPrime(No):
	if No == 1: # 1 is not prime no, prime no needs to have exactly 2 factors 1 & the number itself
		return False
	for i in range(2, int(No/2)+1):
		if No % i == 0:
			return False
	return True

def ListPrime(InputList):
	SumPrime = 0
	for No in InputList:
		if IsPrime(No):
			SumPrime += No
	return SumPrime