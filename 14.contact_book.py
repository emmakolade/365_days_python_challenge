names = []
phone_numbers = []

contact_amount = int(input("how many contact do you want to save: "))
for i in range(contact_amount):
	name = input("Name: ")
	contact_number = input("contact number: ")

	names.append(name)
	phone_numbers.append(contact_number)
print("\n Name \t\t\t Phone Number\n")

for i in range(contact_amount):
	print("{} \t\t\t {}".format(names[i], phone_numbers[i]))

# to search for a contact

search_contact = input("\n enter the contact to search: ")
print("here is the contact")
if search_contact in names:
	index = names.index(search_contact)
	contact_number = phone_numbers[index]
	print(" Name: {}\t Phone Number: {}".format(search_contact, contact_number))
else:
	print("Name not in contact")