source = open("source.py", "r")
output = open("without_comments.py", "w")

for line in source:
    if not line.strip().startswith("#"):
        output.write(line)

source.close()
output.close()

print("Comments removed successfully.")