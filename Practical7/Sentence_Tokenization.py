# Sentence Tokenization

import nltk
nltk.download('punkt')

from nltk.tokenize import sent_tokenize

text = "Python is easy to learn. It is a popular programming language."

sentences = sent_tokenize(text)

print("Sentence Tokens:", sentences)