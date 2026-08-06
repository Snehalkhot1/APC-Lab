import re

html = input("Enter HTML content:\n")

pattern = r'https?://[^\s"<>]+|www\.[^\s"<>]+'

urls = re.findall(pattern, html)

if urls:
    print("\nURLs Found:")
    for url in urls:
        print(url)
else:
    print("No URLs found.")