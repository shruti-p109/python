# Problem Statement details :- 
# Circle class - 3 instances Radius, Area, Circumference - inside init initialise all to 0.0
# one class variable - PI with value 3.14
# 3 instance methods - to accepts user values, cal area, cal circumtances, display results
# Author : Shruti Pimparkar

class Circle:
	# class variable (static - same for all instances of class)
	PI = 3.14

	def __init__(self):
		# instance variables
		self.Radius = 0.0
		self.Area = 0.0
		self.Circumference = 0.0

	def Accept(self):
		print("Enter Radius of circle:")
		self.Radius = float(input())

	def CalculateArea(self):
		self.Area = Circle.PI * self.Radius * self.Radius

	def CalculateCircumference(self):
		self.Circumference = 2 * Circle.PI * self.Radius

	def Display(self):
		print("Circumference of circle is ", self.Circumference)
		print("Area of circle is ", self.Area)

def main():
	# instantiation
	Obj = Circle()
	# call methods
	Obj.Accept()
	Obj.CalculateCircumference()
	Obj.CalculateArea()
	Obj.Display()

if __name__ == "__main__":
	main()