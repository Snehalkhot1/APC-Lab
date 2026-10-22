
from tkinter import *

root = Tk()
root.title("Canvas Example")
root.geometry("250x200")

w = Canvas(root, width=200, height=150)
w.pack()

w.create_line(10, 10, 150, 120)

root.mainloop()
