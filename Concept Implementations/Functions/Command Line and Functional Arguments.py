print('|| Jay Ganesh ||')

print('Command line arguments - using sys.argv, other methods - getopt module,argparse module :-')

import sys
print('argv[0]:',sys.argv[0])
print('argv[1]:',sys.argv[1])
print('argv[2]:',sys.argv[2])

print('Required / Position Arguments :-')

def RequiredKeywordArgDemo(books, price):
	print('Books:', books)
	print('Price:', price)

RequiredKeywordArgDemo('Python-ML Books', 1600)

print('Keyword Arguments')

RequiredKeywordArgDemo(books='Basic python', price=800)

print('Default Arguments :-')

def DefaultArgDemo(books, price=1000):
	print('Books:', books)
	print('Price:', price)

DefaultArgDemo('Python Logic Building')
DefaultArgDemo('Angular',750)
DefaultArgDemo(price=750, books='Angularr')
DefaultArgDemo(books='Angularr')

print('Variable Number of Arguments :-')

def AddNos(*numbers):
	#print(type(numbers)) # tuple
	addition = 0
	for number in numbers:
		addition = addition + number
	return addition

print('AddNos return:',AddNos(10, 20, 30))

print('Keyword Variable Number of Arguments :-')

def PersonalInfo(**info):
	# print(type(info)) # dict
	# print(info.keys())
	# print(info.values())
	# print(type(info.items())) # dict_items
	for key,value in info.items():
		print(key,':',value)
		
PersonalInfo(name='shruti',surname='pimparkar',age=27,mobile=8756423516)