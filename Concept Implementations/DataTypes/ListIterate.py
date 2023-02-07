# Iterate List
# Author : Shruti Pimparkar

def main():
	print("Iterate List")

	# no below loop is faster than other

	data = [11, 21, 51.0, 101]
	print("Iterate using for:")
	for i in data:
		print(i, end=" ")

	print("Iterate using for with index:")
	for i in range(len(data)):
		print("index-"+str(i),data[i])

	print("Iterate using while with index:")
	i = 0
	while i < len(data):
		print(data[i])
		i += 1

if __name__ == "__main__":
	main()