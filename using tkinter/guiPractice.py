from tkinter import *
root = Tk()
newframe = Frame(root)
newframe.pack()

otherframe = Frame(root)
otherframe.pack(side= BOTTOM)

button1 = Button(newframe,text="my button", fg="Red")
button2 = Button(otherframe,text="my other button", fg="Blue")

button1.pack()
button2.pack()
root.mainloop()