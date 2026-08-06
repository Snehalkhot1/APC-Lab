import re

text = input("Enter social media post:\n")

hashtags = re.findall(r'#\w+', text)

if hashtags:
    print("\nHashtags:")
    for tag in hashtags:
        print(tag)
else:
    print("No hashtags found.")