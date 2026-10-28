# Append information to an existing file

file = open("student.txt", "a")

file.write("College: D.Y. Patil College of Engineering and Technology\n")
file.write("City: Kolhapur\n")

file.close()

print("Additional information added successfully.")