dfib = {0: 0, 1: 1}

def fib(x):
	try:
		return dfib[x]
	except KeyError:
		out = fib(x-1) + fib(x-2)
		dfib[x] = out
		return out
		
		
x = int(input("Please enter a natural number: "))
print("The {}th Fibonacci number is: ".format(x) + str(fib(x)))