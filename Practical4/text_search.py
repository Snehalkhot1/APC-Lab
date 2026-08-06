import re

text = input("Enter text:\n")
search = input("Enter word to search: ")

matches = re.findall(search, text, re.IGNORECASE)

print("Occurrences:", len(matches))

highlight = re.sub(search, "**" + search + "**", text, flags=re.IGNORECASE)

print("\nHighlighted Text:")
print(highlight)