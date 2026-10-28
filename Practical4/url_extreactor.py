<<<<<<< HEAD
import re

html = input("Enter HTML content:\n")

pattern = r'https?://[^\s"<>]+|www\.[^\s"<>]+'

urls = re.findall(pattern, html)

if urls:
    print("\nURLs Found:")
    for url in urls:
        print(url)
else:
=======
import re

html = input("Enter HTML content:\n")

pattern = r'https?://[^\s"<>]+|www\.[^\s"<>]+'

urls = re.findall(pattern, html)

if urls:
    print("\nURLs Found:")
    for url in urls:
        print(url)
else:
>>>>>>> origin/main
    print("No URLs found.")