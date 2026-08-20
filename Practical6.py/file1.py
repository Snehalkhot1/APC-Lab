filename = input("Enter the filename : ")
text = input("Enter the text :")
with open(filename, "w") as file:
    file.write(text)
print("File Created Successfully")