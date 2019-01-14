from tkinter import *

root = Tk()

label1 = Label(root, text = "first name")
label2 = Label(root, text="Lastname")

#text field are entrys
entry1 = Entry(root)
entry2 = Entry(root)

#arrange items into the grid format
label1.grid(row=0, column=0)
label2.grid(row=1, column=0)

entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)
root.mainloop()