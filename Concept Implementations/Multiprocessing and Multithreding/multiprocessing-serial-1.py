# display even nos until no
def DisplayEven(No):
	for i in range(No+1):
		if i % 2 == 0:
			print("Even Number:", i)

# display odd nos until no
def DisplayOdd(No):
	for i in range(No+1):
		if i % 2 != 0:
			print("Odd Number:", i)

def main():
	print("Demonstration of Serial Programming:")
	DisplayEven(2000)
	DisplayOdd(2000)

if __name__ == "__main__":
	main()