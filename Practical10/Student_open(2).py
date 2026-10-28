# Display complete contents of a file

file = open("student.txt", "r")

content = file.read()

print(content)

file.close()