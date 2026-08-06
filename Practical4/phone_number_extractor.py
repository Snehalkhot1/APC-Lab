import re

text = input("Enter text:\n")

pattern = r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'

numbers = re.findall(pattern, text)

if numbers:
    print("\nPhone Numbers Found:")
    for num in numbers:
        print(num)
else:
    print("No phone numbers found.")