
from tkinter import *

root = Tk()
root.title("Checkbutton Example")
root.geometry("300x150")

var1 = IntVar()
c1 = Checkbutton(root, text="Male", variable=var1)
c1.pack()

var2 = IntVar()
c2 = Checkbutton(root, text="Female", variable=var2)
c2.pack()

root.mainloop()
