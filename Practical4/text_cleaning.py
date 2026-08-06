import re

text = input("Enter text:\n")

# Convert to lowercase
text = text.lower()

# Expand common contractions
text = text.replace("don't", "do not")
text = text.replace("can't", "cannot")
text = text.replace("won't", "will not")
text = text.replace("i'm", "i am")

# Remove punctuation and special characters
text = re.sub(r'[^a-zA-Z0-9\s]', '', text)

# Remove extra spaces
text = " ".join(text.split())

print("\nCleaned Text:")
print(text)