# Weekly Attendance System

attendance = {
    "Monday": {"Amit", "Sneha", "Rahul"},
    "Tuesday": {"Rahul", "Priya"},
    "Wednesday": {"Amit", "Priya", "Riya"},
    "Thursday": {"Sneha", "Riya"},
    "Friday": {"Amit", "Rahul", "Sneha"}
}

all_students = set()

for students in attendance.values():
    all_students.update(students)

print("Students attended at least one class:")
print(all_students)

common = set.intersection(*attendance.values())
print("\nStudents attended every class:")
print(common)

one_class = set()

for student in all_students:
    count = 0
    for day in attendance:
        if student in attendance[day]:
            count += 1
    if count == 1:
        one_class.add(student)

print("\nStudents attended only one class:")
print(one_class)

print("\nTotal Unique Students:", len(all_students))