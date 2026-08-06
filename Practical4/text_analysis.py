text = input("Enter a paragraph:\n")

words = text.lower().split()

print("Total Words:", len(words))

frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print("\nWord Frequency")
for word, count in frequency.items():
    print(word, ":", count)

sorted_words = sorted(frequency.items(), key=lambda x: x[1], reverse=True)

print("\nTop 3 Frequent Words:")
for word, count in sorted_words[:3]:
    print(word, ":", count)

vowels = "aeiouAEIOU"
count = 0

for ch in text:
    if ch in vowels:
        count += 1

print("\nNumber of Vowels:", count)