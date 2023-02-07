# Author : 				Shruti Pimparkar
# Problem Statement : 	Recursion

def DisplayPattern(No):
	i = 1
	while i <= No:
		print(i, end = " ")
		i += 1

def DisplayPatternR(No):
	if No >= 1:
		DisplayPatternR(No-1)
		print(No, end = " ")


def main():
	print("--- By Iterative Approach ---")
	DisplayPattern(5)
	print("\n--- By Recursive Approach ---")
	DisplayPatternR(5)

if __name__ == "__main__":
	main()