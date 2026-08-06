project1 = {"Amit", "Rahul", "Sneha", "Priya"}
project2 = {"Rahul", "Priya", "Karan", "Riya"}

print("Employees in both projects:")
print(project1.intersection(project2))

print("\nEmployees only in Project 1:")
print(project1.difference(project2))

print("\nEmployees only in Project 2:")
print(project2.difference(project1))

print("\nTotal Unique Employees:")
print(project1.union(project2))