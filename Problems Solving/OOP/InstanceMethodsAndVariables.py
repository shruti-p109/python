# Problem Statement Details :- 
# Demo class - 2 instances no1 & no2
# 2 methods Fun & Gun - displays values of no1 & no2 - instantiate class & call methods
# Author : Shruti Pimparkar

class Demo:
	# class variable initialised to some value
	Value = 'test'

	def __init__(self):
		# initialize instane variables by accepting values from user
		# accept input
		print("Enter a number 1:")
		self.no1 = int(input())
		print("Enter a number 2:")
		self.no2 = int(input())

	def Fun(self):
		print("Inside Demo Fun Function")
		print("Instance variable Values are :", self.no1, self.no2)
		print("Class Variable value :", Demo.Value)
		# modifying class varriable value
		Demo.Value = 'new test'

	def Gun(self):
		print("Inside Demo Gun Function")
		print("Instance variable Values are :", self.no1, self.no2)
		print("Class Variable value :", Demo.Value)

def main():
	# class instantiation
	Obj = Demo()
	# call methods on the object
	Obj.Fun()
	Obj.Gun()

if __name__ == "__main__":
	main()