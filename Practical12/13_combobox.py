
import tkinter as tk
from tkinter import ttk

def on_select(event):
    selected_item = combo_box.get()
    label.config(text="Selected Item: " + selected_item)

root = tk.Tk()
root.title("Combobox Example")
root.geometry("300x150")

label = tk.Label(root, text="Selected Item: ")
label.pack(pady=10)

combo_box = ttk.Combobox(
    root,
    values=["Java", "Python", "C++"]
)
combo_box.pack(pady=5)
combo_box.set("Java")

combo_box.bind("<<ComboboxSelected>>", on_select)

root.mainloop()
