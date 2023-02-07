# Author : 				Shruti Pimparkar
# Problem Statement : 	Recursion

def DisplayPattern(No):
	while No >= 1:
		print(No, end = " ")
		No -= 1

def DisplayPatternR(No):
	if No >= 1:
		print(No, end = " ")
		DisplayPatternR(No-1)

def main():
	print("--- By Iterative Approach ---")
	DisplayPattern(5)
	print("\n--- By Recursive Approach ---")
	DisplayPatternR(5)

if __name__ == "__main__":
	main()