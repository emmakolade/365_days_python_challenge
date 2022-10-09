# program to calculate the BMI of a person 

height = float(input("enter your height in cm: "))
weight = float(input("enter your weight in kf: "))

# to calculate BMI the height has to be in metres.
h = (height/100)**2

BMI = weight / h

print("your BMi is: ", BMI)

if BMI > 0:
	if BMI <= 16:
		print("you are severely underweight")
	elif BMI <= 18.5:
		print("you are underweight")
	elif BMI <= 25:
		print("you are healthy")
	elif BMI <= 30:
		print("you are overweight")
	else:
		print("you are severely overweight")
else: ("enter valid details")
