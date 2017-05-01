def squared(number):
	return number * number

def isEven(number):
	if number % 2 == 0:
		return "yes"
	else:
		return "no"

n = 4
print("squared: " + str(squared(n)))
print("isEven: " + isEven(n))
