# multitasking
# Author : Shruti Pimparkars

# 1 process - on 1 core out of 4

def Square(No):
	return No * No

def main():
	Data = [1, 2, 3, 4, 5]
	Result = list()
	for value in Data:
		Result.append(Square(value))
	print("Result after operation:", Result)

if __name__ == "__main__":
	main()