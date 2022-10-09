import random

#input length of password
length = int(input("enter the length of the password: "))
# possible characters of a password
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!!@#$%^&*()_+-=`,.1234567890"

passwords = "".join(random.sample(characters,length))

print(passwords)