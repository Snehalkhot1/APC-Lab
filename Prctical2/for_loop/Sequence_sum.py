n = int(input("Enter the value of n: "))
sum = 0
fact = 1
for i in range(1, n + 1):
    fact = fact * i
    sum = sum + i + (i / fact)
print("Sum of the Sequence =", sum)