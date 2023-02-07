no = 11

print('Value of no:', no)
print('Datatype of no:', type(no))
print('ID of no:',id(no)) # unique identification number

i = 11

print('Value of i:', i)
print('Datatype of i:', type(i)) # same as no
print('ID of i:',id(i))

i = 12 # value updated

print('Value of updated i:', i)
print('Datatype of updated i:', type(i)) # changed from before
print('ID of updated i:',id(i))

no1, no2, no3 = 11, "21", 51.5 # all these should homogeneous (same type) - why? how is stored in mem - ???
print(no1)
print(id(no1))
print(type(no1))
print(no2)
print(id(no2))
print(type(no2))
print(no3)
print(id(no3))
print(type(no3))