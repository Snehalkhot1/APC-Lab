import re

# Phone Number
phone = input("Enter phone number: ")

if re.fullmatch("[0-9]+", phone) and len(phone) == 10:
    print("Valid Phone Number")
else:
    print("Invalid Phone Number")


# Password
password = input("Enter password: ")

if (re.search("[A-Z]+", password) and
    re.search("[a-z]+", password) and
    re.search("[0-9]+", password) and
    re.search("[@#$]+", password)):
    print("Valid Password")
else:
    print("Invalid Password")


# Email
email = input("Enter email: ")

if re.fullmatch("[A-Za-z]+[0-9]+@gmail.com", email):
    print("Valid Email")
else:
    print("Invalid Email")