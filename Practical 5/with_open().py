# File Handling using with open() 
with open("data.txt", "w") as file:
    file.write("Python File Handling\n\n")
    file.write("Python Programming...!\n")
 
with open("data.txt", "r") as file:
    content = file.read()
 
with open("student.txt", "a") as file:
    file.write("College: D.Y. Patil College\n")

print("File Contents:\n")
print(content)
print("Data appended successfully.")