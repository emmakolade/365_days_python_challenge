#function to convert Fahrenheit to celsius 


def convert(s):
  f = float(s)
# apply formula below
  c = (f - 32) * 5/9
  return c
celsius = input("enter values in Fahrenheit: ")
convert(celsius)

