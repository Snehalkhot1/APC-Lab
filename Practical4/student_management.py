# Student Grade Management System

students = ["Sneha", "Rahul", "Amit"]
grades = [85, 78, 92]

def add_student():
    name = input("Enter student name: ")
    grade = int(input("Enter grade: "))
    students.append(name)
    grades.append(grade)
    print("Student added successfully.")

def update_grade():
    name = input("Enter student name to update: ")
    if name in students:
        index = students.index(name)
        grades[index] = int(input("Enter new grade: "))
        print("Grade updated successfully.")
    else:
        print("Student not found.")

def remove_student():
    name = input("Enter student name to remove: ")
    if name in students:
        index = students.index(name)
        students.pop(index)
        grades.pop(index)
        print("Student removed.")
    else:
        print("Student not found.")

def average_grade():
    avg = sum(grades) / len(grades)
    print("Average Grade:", avg)

def highest_lowest():
    print("Highest Grade:", max(grades))
    print("Lowest Grade:", min(grades))

def display():
    print("\nStudent Records")
    for i in range(len(students)):
        print(students[i], ":", grades[i])

while True:
    print("\n1.Add\n2.Update\n3.Remove\n4.Average\n5.Highest & Lowest\n6.Display\n7.Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        add_student()
    elif choice == 2:
        update_grade()
    elif choice == 3:
        remove_student()
    elif choice == 4:
        average_grade()
    elif choice == 5:
        highest_lowest()
    elif choice == 6:
        display()
    elif choice == 7:
        break
    else:
        print("Invalid Choice")