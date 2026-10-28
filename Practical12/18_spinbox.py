
from tkinter import *

root = Tk()
root.title("Spinbox Example")
root.geometry("300x150")

w = Spinbox(root, from_=0, to=10)
w.pack(pady=30)

root.mainloop()
