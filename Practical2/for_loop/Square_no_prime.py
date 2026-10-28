num = int(input("Enter the number: "))
for i in range(1, num + 1):
    if i * i == num:
        root = i
        break
count = 0
for i in range(1, root + 1):
    if root % i == 0:
        count = count + 1

if count == 2:
  print("The Square-root is Prime Number")
else:
    print("The Square-root is Not a Prime Number")