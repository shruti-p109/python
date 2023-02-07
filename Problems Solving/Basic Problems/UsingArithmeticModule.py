# Program which calls user defined Arithmetic module functions to perform operations on 2 user accepted inputs
# Input: 11 5
# Author : Shruti Pimparkar

from Arithmetic import *

def main():
	print("Enter first number:")
	no1 = int(input())
	print("Enter non-zero second number:")
	no2 = int(input())
	# validation for division by zero
	if no2 == 0:
		print("Can not divide by zero. Please enter non-zero number.")
		exit()
	print(no1,"+",no2,"=",Add(no1,no2))
	print(no1,"-",no2,"=",Sub(no1,no2))
	print(no1,"*",no2,"=",Mult(no1,no2))
	print(no1,"/",no2,"=",Div(no1,no2))

if __name__ == "__main__":
	main()