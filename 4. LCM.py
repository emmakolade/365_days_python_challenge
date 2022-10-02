# function to find the lowest common multiple of two numbers 
num1 = int(input(" enter the first number: "))
num2 = int(input(" enter the second number: "))

def lowest_common_multiple(a, b):

	if a > b:
		greater = a
	elif b > a:
		greater = b 
	while(True):
		if ((greater % a == 0 ) and (greater % b == 0)):
			lcm = greater
			break
		greater = greater + 1
	return lcm

print(lowest_common_multiple(num1, num2))