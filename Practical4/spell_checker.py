<<<<<<< HEAD
dictionary = {
    "python", "program", "computer", "student",
    "college", "science", "engineering",
    "language", "book", "school"
}

text = input("Enter text:\n").lower()

words = text.split()

misspelled = []

for word in words:
    word = word.strip(".,!?")
    if word not in dictionary:
        misspelled.append(word)

print("\nMisspelled Words:")
if misspelled:
    for word in misspelled:
        print(word)
else:
=======
dictionary = {
    "python", "program", "computer", "student",
    "college", "science", "engineering",
    "language", "book", "school"
}

text = input("Enter text:\n").lower()

words = text.split()

misspelled = []

for word in words:
    word = word.strip(".,!?")
    if word not in dictionary:
        misspelled.append(word)

print("\nMisspelled Words:")
if misspelled:
    for word in misspelled:
        print(word)
else:
>>>>>>> origin/main
    print("No misspelled words found.")