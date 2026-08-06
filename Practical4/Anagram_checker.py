# Anagram Checker

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

s1 = ''.join(str1.lower().split())
s2 = ''.join(str2.lower().split())

if sorted(s1) == sorted(s2):
    print("The strings are Anagrams.")
else:
    print("The strings are Not Anagrams.")