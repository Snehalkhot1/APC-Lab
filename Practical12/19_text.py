
from tkinter import *

root = Tk()
root.title("Text Example")
root.geometry("350x150")

T = Text(root, height=2, width=30)
T.pack()

T.insert(END, "Python Tkinter")

root.mainloop()
