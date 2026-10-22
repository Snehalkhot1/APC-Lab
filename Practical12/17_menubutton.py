
from tkinter import *

root = Tk()
root.title("Menubutton Example")
root.geometry("300x150")

mb = Menubutton(root, text="Click here")
mb.menu = Menu(mb, tearoff=0)
mb["menu"] = mb.menu

cVar = IntVar()
aVar = IntVar()

mb.menu.add_checkbutton(label="Contact", variable=cVar)
mb.menu.add_checkbutton(label="About", variable=aVar)

mb.pack(pady=30)

root.mainloop()
