def display_employees():
    file = open("employees.txt", "r")

    for line in file:
        data = line.strip().split(",")

        print("ID:", data[0],
              "Name:", data[1],
              "Department:", data[2],
              "Salary:", data[3])

    file.close()


def highest_paid():
    file = open("employees.txt", "r")

    highest = None

    for line in file:
        data = line.strip().split(",")
        salary = int(data[3])

        if highest is None or salary > highest[3]:
            highest = [data[0], data[1], data[2], salary]

    file.close()

    print("Highest Paid Employee:", highest[1])
    print("Salary:", highest[3])


def average_salary():
    file = open("employees.txt", "r")

    total = 0
    count = 0

    for line in file:
        data = line.strip().split(",")
        total = total + int(data[3])
        count = count + 1

    file.close()

    print("Average Salary:", total / count)


def above_salary(amount):
    file = open("employees.txt", "r")

    print("Employees earning above", amount)

    for line in file:
        data = line.strip().split(",")

        if int(data[3]) > amount:
            print(data[1], data[3])

    file.close()


display_employees()
print()

highest_paid()
print()

average_salary()
print()

above_salary(50000)