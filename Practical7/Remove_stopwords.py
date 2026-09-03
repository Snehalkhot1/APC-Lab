# Remove Stopwords

import nltk
nltk.download('stopwords')

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

text = "This is a simple example of text processing."

words = word_tokenize(text)

stop_words = set(stopwords.words('english'))

filtered_words = []

for word in words:
    if word.lower() not in stop_words:
        filtered_words.append(word)

print("Original Words:", words)
print("After Removing Stopwords:", filtered_words)