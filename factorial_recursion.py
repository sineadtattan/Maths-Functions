def factorial(n):
	"""
	Calculate the factorial of the input n

	:type n: int
	:param n: the parameter we want to calculate the factorial of

	:rtype: int
	"""
	if n <= 1:
		return 1
	else:
		return n*factorial(n-1)

x = 6

result = factorial(x)

print(result)