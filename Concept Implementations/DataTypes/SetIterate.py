# Iterate set
# Author : Shruti Pimparkar

def main():
	print("Iterate Set")

	# no below loop is faster than other

	data = {11, 21, 51.0, 101, "helllooo"}
	print("Iterate using for:")
	for i in data:
		print(i, end=" ")
	print("\n-----------------")

	# print("Iterate using for with index:") # TypeError: 'set' object is not subscriptable - no index
	# for i in range(len(data)):
	# 	print("index-"+str(i),data[i])
	# print("\n-----------------")

	# print("Iterate using while with index:") # TypeError: 'set' object is not subscriptable - no index
	# i = 0
	# while i < len(data):
	# 	print(data[i], end=" ")
	# 	i += 1

if __name__ == "__main__":
	main()