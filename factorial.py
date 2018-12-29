def factorial(n):
	"""
	Calculate the factorial of the input n

	:type n: int
	:param n: the parameter we want to calculate the factorial of

	:rtype: int
	"""
	f = 1
	for i in range(1,n+1):
		f = f*i

	return f



x = 1000

result = factorial(x)