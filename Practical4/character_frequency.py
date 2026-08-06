# Character Frequency Counter

text = input("Enter a string: ")

choice = input("Ignore case? (yes/no): ")

if choice.lower() == "yes":
    text = text.lower()

frequency = {}

for ch in text:
    frequency[ch] = frequency.get(ch, 0) + 1

sorted_frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)

print("\nCharacter Frequency:")

for char, count in sorted_frequency:
    print(f"'{char}' : {count}")