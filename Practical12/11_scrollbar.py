
from tkinter import *

root = Tk()
root.title("Scrollbar Example")
root.geometry("300x300")

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

mylist = Listbox(root, yscrollcommand=scrollbar.set)

for line in range(100):
    mylist.insert(END, "Line - " + str(line))

mylist.pack(side=LEFT, fill=BOTH, expand=True)

scrollbar.config(command=mylist.yview)

root.mainloop()
