stopwords = {
    "is", "the", "a", "an", "and",
    "to", "of", "in", "on", "at",
    "for", "with"
}

text = input("Enter paragraph:\n")

words = text.split()

result = []

for word in words:
    if word.lower() not in stopwords:
        result.append(word)

print("\nAfter Removing Stopwords:")
print(" ".join(result))
