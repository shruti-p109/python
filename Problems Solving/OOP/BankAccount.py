# Author : 				Shruti Pimparkar
# Problem Statement : 	OOPS Concepts - Instance methods, variables, Class Variables (BankAccount)

class BankAccount:

	ROI = 10.5 # yearly

	def __init__(self, Name, Amount):
		self.Name = Name
		self.Amount = Amount

	def Display(self):
		print("Customer Name:", self.Name)
		print("Customer Account Amount:", self.Amount)

	def Deposit(self, DepositAmount):
		self.Amount += DepositAmount

	def Withdraw(self, WithdrawAmount):
		self.Amount -= WithdrawAmount

	def CalculateInterest(self):
		return self.Amount * BankAccount.ROI * 1

def main():
	print("Enter First Customer Name:")
	Name1 = input()
	print("Enter First Customer Account Amount:")
	Amount1 = int(input())

	# instance 1
	BankAccountObj1 = BankAccount(Name1, Amount1)
	print("--- Calling Display Method ---")
	BankAccountObj1.Display()
	print("--- Calling Deposit Method with 2000 Amount ---")
	BankAccountObj1.Deposit(2000)
	print("--- Calling Withdraw Method with 1000 Amount ---")
	BankAccountObj1.Withdraw(1000)
	print("--- Calling Display Method ---")
	BankAccountObj1.Display()
	print("Simple Interest is:", BankAccountObj1.CalculateInterest())


	print("Enter Second Customer Name:")
	Name2 = input()
	print("Enter Second Customer Account Amount:")
	Amount2 = int(input())

	# instance 1
	BankAccountObj2 = BankAccount(Name2, Amount2)
	print("--- Calling Display Method ---")
	BankAccountObj2.Display()
	print("--- Calling Deposit Method with 1500 Amount ---")
	BankAccountObj2.Deposit(1500)
	print("--- Calling Withdraw Method with 500 Amount ---")
	BankAccountObj2.Withdraw(500)
	print("--- Calling Display Method ---")
	BankAccountObj2.Display()
	print("Simple Interest is:", BankAccountObj2.CalculateInterest())

if __name__ == "__main__":
	main()

