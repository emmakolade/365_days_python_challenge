def ip_address(address):
	new_address = ""
	split_address = address.split(".")
	separator = "[.]"

	new_address = separator.join(split_address)
	return new_address

IP = input("enter your IP address: ")
ipAddress = ip_address(IP)
print(ipAddress)