import os
 
directory = "MyFolder"
 
if not os.path.exists(directory):
    os.mkdir(directory)
    print("Directory created successfully.")
else:
    print("Directory already exists.")
 
print("\nCurrent Working Directory:")
print(os.getcwd())
 
print("\nContents of Current Directory:")
print(os.listdir())
 
new_directory = "NewFolder"

if os.path.exists(directory):
    os.rename(directory, new_directory)
    print("\nDirectory renamed successfully.")
 
print("\nContents after renaming:")
print(os.listdir())

print("\nNew directory location:")
print(os.path.abspath(new_directory))