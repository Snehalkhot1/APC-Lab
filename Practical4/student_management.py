students = []
grades = []

def add_student(name, grade):
    students.append(name)
    grades.append(grade)

def update_grade(name, grade):
    if name in students:
        index = students.index(name)
        grades[index] = grade
    else:
        print("Student not found")

def remove_student(name):
    if name in students:
        index = students.index(name)
        students.pop(index)
        grades.pop(index)
    else:
        print("Student not found")

def display_result():
    if len(grades) == 0:
        print("No students available")
        return

    print("Students:", students)
    print("Grades:", grades)
    print("Average Grade:", sum(grades) / len(grades))
    print("Highest Grade:", max(grades))
    print("Lowest Grade:", min(grades))

add_student("Snehal Khot", 95)
add_student("Madhuri Farakate", 82)
add_student("Maithili Raut", 81)

update_grade("Maithili Raut", 90)
remove_student("Madhuri Farakate")

display_result()