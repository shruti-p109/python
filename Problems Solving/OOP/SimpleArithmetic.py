# Problem Statement details :- 
# Arithmetic class - 2 instance variables - Value1, Value2 - inside init initialise all to 0
# 3 instance methods - to accepts user values, cal addition & return, cal subtraction, cal multiplication, cal division, display results
# Author : Shruti Pimparkar

class Arithmetic:
	def __init__(self):
		# instance variables
		self.value1 = 0
		self.value2 = 0

	# accept values from user and set them in instance variables value1 & value2
	def Accept(self):
		print("Enter number 1:")
		self.value1 = int(input())
		print("Enter number 2:")
		self.value2 = int(input())

	# perform addition & return result
	def Addition(self):
		return self.value1 + self.value2

	def Subtraction(self):
		return self.value1 - self.value2

	def Multiplication(self):
		return self.value1 * self.value2

	def Division(self):
		return self.value1 / self.value2

def main():
	Obj = Arithmetic()
	# accept values
	Obj.Accept()
	# perform operations & display
	print("Addition of numbers is", Obj.Addition())
	print("Subtraction of numbers is", Obj.Subtraction())
	print("Multiplication of numbers is", Obj.Multiplication())
	print("Division of numbers is", Obj.Division())

if __name__ == "__main__":
	main()