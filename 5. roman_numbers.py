# function to convert roman numbers to decimal 

romans = {
	"I": 1, 
	"V": 5,
	"X": 10,
	"XL": 40,
	"L": 50,
	"XC": 90,
	"C": 100,
	"CD": 400,
	"D": 500,
	"CM": 900,
	"M": 1000
} #dictionary of Roman Numerals 

def RomantoDecimal(romanNumeral):
	sum = 0
	for i in range(len(romanNumeral) - 1):
		left = romanNumeral[i]
		right = romanNumeral[i + 1]
		if romans[left] < romans[right]:
			sum -= romans[left]
		else:
			sum += romans[left]
	sum += romans[romanNumeral[-1]]
	return sum
roman_input = input("enter roman numbers: ")
print(RomantoDecimal(roman_input))
