# Word Tokenization

import nltk
nltk.download('punkt')

from nltk.tokenize import word_tokenize

text = "Python is easy to learn."

words = word_tokenize(text)

print("Word Tokens:", words)