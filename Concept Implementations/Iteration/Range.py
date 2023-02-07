# range (start, end, displacement)

# start by default 0
# displacement by default 1
# end - no default value - mandatory by user - exclusive (if 5 will stop at 4)

# print(range(1,5)) # printed as it is - range(1,5) - you have to iterate it !!

# range(1,5) # 1 2 3 4
# range(1,5,1) # 1 2 3 4
# range(1,7,2) # 1 3 5

for i in range(1,5):
	print(i)

print("--------------------")

for i in range(1,7,2):
	print(i) # print prints \n at the end by default, you can change it for eg. by setting end=,

print("--------------------")

print(i) # prints last value of i, scope of i - beyond for loop