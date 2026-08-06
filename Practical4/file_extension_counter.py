import re

files = input("Enter file names separated by space:\n").split()

extensions = {}

for file in files:
    match = re.search(r'\.([A-Za-z0-9]+)$', file)
    if match:
        ext = match.group(1)
        extensions[ext] = extensions.get(ext, 0) + 1

print("\nExtension Count:")
for ext, count in extensions.items():
    print(ext, ":", count)