book1 = input("Enter text of Book 1: ").lower().split()
book2 = input("Enter text of Book 2: ").lower().split()

set1 = set(book1)
set2 = set(book2)

print("Unique words in Book 1:", set1)
print("Unique words in Book 2:", set2)
print("Common words:", set1 & set2)
print("Only in Book 1:", set1 - set2)
print("Only in Book 2:", set2 - set1)
print("Total Unique Words:", len(set1 | set2))
