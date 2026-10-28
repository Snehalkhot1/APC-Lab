
from tkinter import *

root = Tk()
root.title("Listbox Example")
root.geometry("300x200")

lb = Listbox(root)
lb.insert(1, "Python")
lb.insert(2, "Java")
lb.insert(3, "C++")
lb.insert(4, "Any other")

lb.pack()

root.mainloop()
