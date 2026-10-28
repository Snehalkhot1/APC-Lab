file = open("student.txt", "r")

content = file.read().lower()
words = content.split()

frequency = {}

for word in words:
    if word in frequency:
        frequency[word] = frequency[word] + 1
    else:
        frequency[word] = 1

print("Word Frequency:")

for word in frequency:
    print(word, ":", frequency[word])

file.close()