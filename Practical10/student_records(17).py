file = open("students.txt", "r")

file.readline()

students = []

for line in file:
    data = line.strip().split(",")

    roll = int(data[0])
    name = data[1]
    marks = int(data[2])

    students.append([roll, name, marks])

file.close()

print("All Records:")

for student in students:
    print(student[0], student[1], student[2])

highest = students[0]

for student in students:
    if student[2] > highest[2]:
        highest = student

print("\nHighest Marks:")
print(highest[1], highest[2])

total = 0

for student in students:
    total = total + student[2]

average = total / len(students)

print("\nAverage Marks:", average)

print("\nStudents scoring more than 80:")

for student in students:
    if student[2] > 80:
        print(student[1], student[2])