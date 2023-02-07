# Author : 				Shruti Pimparkar
# Problem Statement : 	Recursion

# iterative approach using while
def DisplayPattern(No):
	i = 1
	while i <= No:
		print("*", end = " ")
		i += 1

# recursive approach using while
def DisplayPatternR(No):
	if No > 0:
		print("*", end = " ")
		DisplayPatternR(No-1)

def main():
	print("--- By Iterative Approach ---")
	DisplayPattern(5)
	print("\n--- By Recursive Approach ---")
	DisplayPatternR(5)

if __name__ == "__main__":
	main()