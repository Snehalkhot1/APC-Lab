import re

text = input("Enter a word or sentence: ")

# Convert to lowercase
text = text.lower()

# Remove spaces and punctuation
text = re.sub(r'[^a-z0-9]', '', text)

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")