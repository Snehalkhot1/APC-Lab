
from tkinter import *

root = Tk()
root.title("Entry Example")
root.geometry("350x150")

Label(root, text="First Name").grid(row=0, column=0)

e1 = Entry(root)
e1.grid(row=0, column=1)

root.mainloop()
