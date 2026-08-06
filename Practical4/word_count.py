import string

filename = input("Enter text file name: ")

try:
    with open(filename, "r") as file:
        text = file.read().lower()

    # Remove punctuation
    for ch in string.punctuation:
        text = text.replace(ch, "")

    words = text.split()

    frequency = {}

    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    print("Total Words:", len(words))

    print("\nTop 10 Frequent Words:")
    sorted_words = sorted(frequency.items(), key=lambda x: x[1], reverse=True)

    for word, count in sorted_words[:10]:
        print(word, ":", count)

except FileNotFoundError:
    print("File not found.")