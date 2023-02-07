# making it user interactive

print("Application to demonstrate industrial programming")

def main():
	print("Enter first number:")
	# no1 = input() # 10
	no1 = int(input())
	# print(type(no1))
	print("Enter second number:")
	no2 = input() # 11
	# print(type(no2))
	# ans = no1 + no2 # 1011 - concatenation like strings - no format specifier - input always will give str value - convert it into whatever you want
	ans = no1 + int(no2) # type conversion # preferred way over int(input()) - prefer temp (only when you need) conversion - BUT if you need converted value frequently forward int(input()) is preferred

	print("Addition is:",ans)

if __name__ == "__main__": # special / dunder (double under score) variable # is current modules files name __main__ ?
	main()


