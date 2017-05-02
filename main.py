def squared(n):
	return n * n

def cubed(n):
	return n * n * n

def power(n, p):
	return n ** p

def isEven(n):
	if n % 2 == 0:
		return "yes"
	else:
		return "no"

n = 4
print("squared: " + str(squared(n)))
print("cubed: " + str(cubed(n)))
print("isEven: " + isEven(n))
print("power of 5: " + str(power(n, 5)))
