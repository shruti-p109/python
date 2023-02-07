# reusability - separate out business logic from main function and keep it in a function callable (reusable) from somewhere else
# service provider functions - avoid print, input statements - shift them in main - make those functions sharable at organic level

print("Application to demonstrate industrial programming")

def Addition(value1, value2):
	# business logic - input - do something with/on it - output
	return value1 + value2 # no need to specify return type


def main(): # user input - output keep it in main
	print("Enter first number:")
	no1 = int(input())
	print("Enter second number:")
	no2 = int(input())

	print("Addition is:", Addition(no1, no2)) # send type converted values to business logic function, don't make them do coversions - this makes them more generic

if __name__ == "__main__":
	main()

# no need of function overloading in python - arguments of functions can be of any data type

#execution
# indentation 0 lines - 4,6,11,19 - 6,11 dependable skipped - 4 run - 19 run - 11 block inside - take inputs - memory allocated - 17 - 6 block - return from 6 block (8) - 17 - display - 21

# drawbacks
# how to share Addition function outside file - it needs to be in separate file for that - module (any .py file which contains functions you want to share)


