import re
text = "Python is easy to learn."
result = re.search("Python", text)
if result:
    print("Word found")
else:
    print("Word not found") 