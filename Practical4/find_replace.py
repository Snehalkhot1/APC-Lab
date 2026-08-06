filename = input("Enter file name: ")

find_word = input("Word to find: ")
replace_word = input("Replace with: ")

try:
    with open(filename, "r") as file:
        text = file.read()

    count = text.count(find_word)

    text = text.replace(find_word, replace_word)

    with open("updated_" + filename, "w") as file:
        file.write(text)

    print("Occurrences Found:", count)
    print("Updated file saved as:", "updated_" + filename)

except FileNotFoundError:
    print("File not found.")