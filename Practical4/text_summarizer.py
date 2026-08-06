import re

text = input("Enter paragraph:\n")

sentences = re.split(r'(?<=[.!?])\s+', text)

print("\nSentences:")

for i, sentence in enumerate(sentences, start=1):
    print(i, ".", sentence)