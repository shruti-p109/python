# Author : 				Shruti Pimparkar
# Problem Statement : 	OOPS Concepts - Instance methods, variables, Class Variables (Arithmetic)

class Arithmetic:
	
	def __init__(self, Value):
		self.Value = Value

	def Factors(self):
		print("Factors of", self.Value, "are:")
		for i in range(1, int(self.Value / 2) + 1):
			if self.Value % i == 0:
				print(i, end = " ")
		print()

	def SumFactors(self): # excluding the number itself
		Sum = 0
		for i in range(1, int(self.Value / 2) + 1):
			if self.Value % i == 0:
				Sum += i
		return Sum

	def ChkPrime(self):
		if self.SumFactors() == 1:
			return True
		else:
			return False

	def ChkPerfect(self):
		Flag = False
		if self.SumFactors() == self.Value:
			Flag = True
		return Flag

def main():
	print("Enter first integer:")
	ArithmeticObj1 = Arithmetic(int(input()))
	ArithmeticObj1.Factors()
	print("Factors Sum is:", ArithmeticObj1.SumFactors())
	if ArithmeticObj1.ChkPrime():
		print("Number is prime")
	else:
		print("Number is not prime")
	if ArithmeticObj1.ChkPerfect():
		print("Number is perfect")
	else:
		print("Number is not perfect")

	# 2nd object
	print("Enter second integer:")
	ArithmeticObj2 = Arithmetic(int(input()))
	ArithmeticObj2.Factors()
	print("Factors Sum is:", ArithmeticObj2.SumFactors())
	if ArithmeticObj2.ChkPrime():
		print("Number is prime")
	else:
		print("Number is not prime")
	if ArithmeticObj2.ChkPerfect():
		print("Number is perfect")
	else:
		print("Number is not perfect")


if __name__ == "__main__":
	main()

