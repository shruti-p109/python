values = [10, 20, 30, 40, 50] # indexes - 0 1 2 3 4 - look at list from range() pov - start at 0 (always), end at 4 (can change dep on len of list), displacement of 1 (always)

# end needs to be 5 -> len of list 

for i in range(0,len(values),1): # 1 (displacement) need not be stated explicitly as default value is same -> 1
	print(i)
	print(values[i])

print("----------------------")

for i in range(0,len(values)):
	print(i)
	print(values[i])

print("----------------------")

for no in values: # like foreach loop - no access to indices
	print(no)
