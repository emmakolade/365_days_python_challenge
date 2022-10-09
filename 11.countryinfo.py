from countryinfo import CountryInfo

count = input("enter your country: ")

country = CountryInfo(count)

print("capital is: ", country.capital())
print("currency is: ", country.currencies())
print("language is: ", country.lanquage())
print("borders are: ", country.borders())
print("other names: ", country.alt_spellings())

