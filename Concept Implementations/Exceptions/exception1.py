# interrupt
# error - before prg exection - something went wrong - unable to start - its a serious problem and a reasonable appln should not try to catch it
# exception - running prg - something went wrong run time

# exception handler - prevents abnormal termination of prg

# c lang errors-
# preprocessing error - # file include
# cpu did not get register - assembly time error
# prg dep on other prg - error on linking - link time
# compile time error - wrong prg (syntax)
# loader - exe - from hd to ram - ram full - prg unable to load on ram - load time error
# while running - error - run time error

def main():
	try: # exception prone code
		print("Enter first number:")
		No1 = int(input())
		print("Enter second number:")
		No2 = int(input())
		Ans = No1 / No2
		print("Division is:",Ans)
	# except ZeroDivisionError: # exception handler
	# 	print("inside ZeroDivisionError exception handler")
	# except ValueError: # if you enter non-int as input
	# 	print("inside ValueError exception handler")
	except Exception as e: # will catch / handle any type of exception - generalized except/catch block
		print("Inside last except block:",type(e)) # <class 'ZeroDivisionError'>
		print("Exception name:", type(e).__name__) # 'ZeroDivisionError'
		print("Exception args:", e.args) # ('division by zero',)
		print("Type of type of exception:", type(type(e))) # <class 'type'>
	finally:
		print("Inside finally block")

if __name__ == "__main__":
	main()