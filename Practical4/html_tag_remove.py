import re

html = input("Enter HTML:\n")

clean_text = re.sub(r'<.*?>', '', html)

print("\nText without HTML Tags:")
print(clean_text)