import re

text = input("Enter text:\n")

pattern = r'\b\d{2}/\d{2}/\d{4}\b|\b\d{4}-\d{2}-\d{2}\b|\b\d{4}/\d{2}/\d{2}\b|\b[A-Za-z]+ \d{1,2}, \d{4}\b'

dates = re.findall(pattern, text)

if dates:
    print("\nDates Found:")
    for date in dates:
        print(date)
else:
    print("No dates found.")