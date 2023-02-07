# Anonymus Function / Lambda Function
# Author : Shruti Pimparkar

# write first - Normal isEven Function
def isEven(No):
	# if No % 2 == 0:
	# 	return True
	# else:
	# 	return False

	# compact code of above
	# == - one of the relational operatora - always returns True or False
	return No % 2 == 0

# convert normal function to lambda function
isEvenLambda = lambda No : No % 2 == 0


def main():
	if(isEven(12)):
		print("its even")
	else:
		print("its odd")

	print("Using Lambda Function")
	if(isEvenLambda(12)):
		print("its even")
	else:
		print("its odd")


# starter - from where execution starts
if 	__name__ == "__main__":
	main()
