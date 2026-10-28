<<<<<<< HEAD
import re

html = input("Enter HTML:\n")

clean_text = re.sub(r'<.*?>', '', html)

print("\nText without HTML Tags:")
=======
import re

html = input("Enter HTML:\n")

clean_text = re.sub(r'<.*?>', '', html)

print("\nText without HTML Tags:")
>>>>>>> origin/main
print(clean_text)