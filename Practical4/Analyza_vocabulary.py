book1 = input("Enter Book 1 text:\n").lower().split()
book2 = input("\nEnter Book 2 text:\n").lower().split()

set1 = set(book1)
set2 = set(book2)

print("\nUnique words in Book 1:")
print(set1)

print("\nUnique words in Book 2:")
print(set2)

print("\nCommon Words:")
print(set1.intersection(set2))

print("\nWords only in Book 1:")
print(set1.difference(set2))

print("\nWords only in Book 2:")
print(set2.difference(set1))

print("\nTotal Unique Words Across Both Books:")
print(set1.union(set2))