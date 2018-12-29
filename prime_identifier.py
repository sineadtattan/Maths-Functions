def is_prime(n):
	"""
	Return 'True' if 'n' is a prime number. False otherwise

	:type n: int
	:param n: we want to find whether this parameter is prime or not
	:rtype: boo
	"""
	if n == 1:
		return False

	for i in range(2, n):
		if n % i == 0:
			return False
	return True

x = int(raw_input("Type in any natural number: "))

result = is_prime(x)

print(result)