def squared(n):
	return n * n

def isEven(n):
	if n % 2 == 0:
		return "yes"
	else:
		return "no"

def cubed(n):
	return n * n * n

n = 4
print("squared: " + str(squared(n)))
print("cubed: " + str(cubed(n)))
print("isEven: " + isEven(n))
