
import tkinter as tk

root = tk.Tk()
root.title("Button Example")
root.geometry("300x150")

button = tk.Button(
    root,
    text="Stop",
    width=25,
    command=root.destroy
)
button.pack()

root.mainloop()
