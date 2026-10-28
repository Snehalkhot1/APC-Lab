
from tkinter import *

root = Tk()
root.title("Scale Example")
root.geometry("300x250")

w1 = Scale(root, from_=0, to=42)
w1.pack()

w2 = Scale(
    root,
    from_=0,
    to=200,
    orient=HORIZONTAL
)
w2.pack()

root.mainloop()
