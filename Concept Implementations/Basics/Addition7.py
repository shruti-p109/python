# reusability - business logic - separate module

import MyModule
# from MyModule import Addition # .pyc files get implicitly created - why? - R - share .pyc instead of .py file of module

print("Application to demonstrate industrial programming")

def main():
	print("Special variable __name__ value from main:",__name__) # MarvellousModule - module name as execution starts from there
	print("Enter first number:")
	no1 = int(input())
	print("Enter second number:")
	no2 = int(input())

	print("Addition is:", MarvellousModule.Addition(no1, no2)) # NameError: name 'Addition' is not defined - import module to use it
	# print("Addition is:", Addition(no1, no2))

if __name__ == "__main__":
	main()
