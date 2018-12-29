def fibonacci(n):
	"""
	Determines the value of a term in the Fibonacci sequence

	:type n: int
	:param n: the term of the fibonacci sequence
	:rtype: int
	"""
	if n == 1:
		return 1
	elif n == 2:
		return 1
	elif n > 2:
		return fibonacci(n-1) + fibonacci(n-2)

for n in range(1,11):
	print(n, ":", fibonacci(n))