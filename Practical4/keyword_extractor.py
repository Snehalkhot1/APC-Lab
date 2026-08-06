text = input("Enter text:\n").lower()

stopwords = {
    "the", "is", "a", "an", "and",
    "of", "to", "in", "on", "for",
    "with", "this", "that"
}

words = text.split()

frequency = {}

for word in words:
    word = word.strip(".,!?")
    if word not in stopwords:
        frequency[word] = frequency.get(word, 0) + 1

sorted_words = sorted(frequency.items(), key=lambda x: x[1], reverse=True)

print("\nTop 5 Keywords:")
for word, count in sorted_words[:5]:
    print(word, ":", count)