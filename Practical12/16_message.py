
from tkinter import *

root = Tk()
root.title("Message Example")
root.geometry("300x150")

ourMessage = "This is our Message"

messageVar = Message(root, text=ourMessage)
messageVar.config(bg="lightgreen")
messageVar.pack()

root.mainloop()
