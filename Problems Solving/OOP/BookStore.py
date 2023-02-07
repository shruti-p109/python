# Author : 				Shruti Pimparkar
# Problem Statement : 	OOPS Concepts - Instance methods, variables, Class Variables (BookStore)

class BookStore:
	# class variable
	NoOfBooks = 0

	# constructor
	def __init__(self, Name, Author):
		# instance variables
		self.Name = Name
		self.Author = Author
		BookStore.NoOfBooks += 1

	# instance method
	def Display(self):
		# accessing instance variables inside instance method
		print("Name of Book:", self.Name)
		print("Name of Author:", self.Author)
		# accessing class variable inside instance method
		print("No of Books:", BookStore.NoOfBooks)

def main():
	print("Enter Name of Book:")
	Book1 = input()
	print("Enter Name of Author:")
	Author1 = input()

	# instance 1
	BookStoreObj1 = BookStore(Book1, Author1)
	BookStoreObj1.Display()

	print("Enter Name of Book:")
	Book2 = input()
	print("Enter Name of Author:")
	Author2 = input()

	# instance 2
	BookStoreObj2 = BookStore(Book2, Author2)
	BookStoreObj2.Display()

if __name__ == "__main__":
	main()

