import re

email = input("Enter Email Address: ")

pattern = r'^[A-Za-z0-9._-]+@[A-Za-z0-9-]+\.[A-Za-z]{2,6}$'

if re.match(pattern, email):
    print("Valid Email Address")
else:
    print("Invalid Email Address")