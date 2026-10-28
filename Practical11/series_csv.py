import csv
from datetime import date, datetime

# Get current system date
today = date.today()

# Open CSV file
with open("Practical11/students.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        name = row["name"]
        roll = row["roll"]
        birthday = datetime.strptime(row["birthday"], "%Y-%m-%d").date()

        # Calculate age
        age = today.year - birthday.year

        # Check if birthday has occurred this year
        if (today.month, today.day) < (birthday.month, birthday.day):
            age = age - 1

        print("Name:", name)
        print("Roll:", roll)
        print("Birthday:", birthday)
        print("Current Date:", today)
        print("Age:", age)
        print("-------------------------")