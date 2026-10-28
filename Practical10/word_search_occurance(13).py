word = input("Enter word to search: ")

file = open("student.txt", "r")

count = 0
line_number = 0

for line in file:
    line_number = line_number + 1
    words = line.split()

    for w in words:
        if w.lower() == word.lower():
            count = count + 1
            print("Word found on line:", line_number)

print("Total occurrences:", count)

file.close()