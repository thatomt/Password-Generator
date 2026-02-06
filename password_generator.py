import random
#List of the characters needed to create our password, including symbols
password_characters = "abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+?><"

password = " "
for i in range(12):
    password += random.choice(password_characters)

print("Your password is:  ", password)
print(password)
