<<<<<<< HEAD
import re

password = input("Enter Password: ")

pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%^&+=!]).{8,}$'

if re.match(pattern, password):
    print("Strong Password")
else:
=======
import re

password = input("Enter Password: ")

pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%^&+=!]).{8,}$'

if re.match(pattern, password):
    print("Strong Password")
else:
>>>>>>> origin/main
    print("Weak Password")