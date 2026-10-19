import tkinter as tk
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("Welcome Application")
root.geometry("350x250")

# Heading
label = tk.Label(
    root,
    text="Welcome to Python GUI",
    font=("Arial", 16)
)
label.pack(pady=15)

# Name label
name_label = tk.Label(root, text="Enter your name:")
name_label.pack()

# Input box
name_entry = tk.Entry(root)
name_entry.pack(pady=5)

# Button function
def greet():
    name = name_entry.get()

    if name.strip() == "":
        messagebox.showwarning(
            "Warning", "Please enter your name"
        )
    else:
        messagebox.showinfo(
            "Welcome", "Hello, " + name + "!"
        )

# Button
button = tk.Button(
    root,
    text="Submit",
    command=greet
)
button.pack(pady=15)

# Run the application
root.mainloop()