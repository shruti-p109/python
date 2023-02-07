# Anonymus Function / Lambda Function
# Author : Shruti Pimparkar

# Normal Function / Named Function
def Add(No1, No2):
	return No1 + No2

# Lambda Function
# syntax :- func_name = lambda func_parameters : func_body
# limitation - func defination needs to be one line logic, no if else and all	
# like inline func in c++
# AddFunction - like function pointer in c
AddLambda = lambda No1, No2 : No1 + No2

def main():
	print("Addition by normal func", Add(10,11))
	print("Addition by lambda func", AddLambda(10,11))
	print(type(AddLambda)) # <class 'function'>
	print(type(Add)) # <class 'function'>
	print(id(Add))

# starter - from where execution starts
if 	__name__ == "__main__":
	main()
