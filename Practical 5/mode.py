## with open() function
with open("student.txt", "w") as file:
    file.write("Snehal\n")
    file.write("Rahul\n")
    file.write("Priya\n")
    file.write("Amit\n")
print("1. Data written successfully using w mode.")
with open("student.txt", "r") as file:
    content = file.read()

##read the data
print("\n2. Data read using r mode:")
print(content)
with open("student.txt", "r") as file:
    line = file.readline()

## read one line
print("3. Using readline():")
print(line)
with open("student.txt", "r") as file:
    lines = file.readlines()

## read all the lines
print("4. Using readlines():")
print(lines)


with open("student.txt", "a") as file:
    file.write("Neha\n")
    file.write("Vishal\n")
print("\n5. Data appended successfully using a mode.")
with open("student.txt", "r") as file:
    print(file.read())



with open("student.txt", "r+") as file:
    content = file.read()
    print("6. Data using r+ mode:")
    print(content)
    file.write("Kiran\n")
print("Data written using r+ mode.")


with open("student_wplus.txt", "w+") as file:
    file.write("Python\n")
    file.write("Java\n")
    file.write("C++\n")
    file.seek(0)
    content = file.read()
print("\n7. Data using w+ mode:")
print(content)



with open("student_aplus.txt", "a+") as file:
    file.write("HTML\n")
    file.write("CSS\n")
    file.seek(0)
    content = file.read()
print("8. Data using a+ mode:")
print(content)



try:
    with open("new_student.txt", "x") as file:
        file.write("This file is created using x mode.\n")
    print("9. File created successfully using x mode.")
except FileExistsError:
    print("9. File already exists, so x mode cannot create it again.")
print("\nFinal content of student.txt:")

with open("student.txt", "r") as file:
    print(file.read())