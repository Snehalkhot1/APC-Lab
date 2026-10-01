# Create a file and write student information

file = open("student.txt", "w")

file.write("Name: Snehal Khot\n")
file.write("Roll Number: 45\n")
file.write("Branch: Computer Science and Engineering\n")
file.write("Semester: 5th Semester\n")

file.close()

print("Student information written successfully.")