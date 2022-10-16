from forex_python.converter import CurrencyRates

c_rates = CurrencyRates()
amount =int(input("enter the amount to convert"))

from_currency = input("from which currency: ").upper()
to_currecncy = input("to which currency: ").upper()

print(from_currency, " To ", to_currecncy, amount)
res = c_rates.convert(from_currency, to_currecncy, amount)
print(res)
