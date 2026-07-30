text = input("Enter message: ")
shift = int(input("Enter shift: "))
result = ""
for ch in text:
    if ch.isalpha():
        start = ord('A') if ch.isupper() else ord('a')
        result += chr((ord(ch)-start+shift)%26+start)
    else:
        result += ch
print("Encrypted:", result)