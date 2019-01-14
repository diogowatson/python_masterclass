#creating a status bar
from tkinter import *

def function1():
    print("Menu item cliked")

root= Tk()

#creating menus usinf buidd-in classes
mymenu = Menu(root)
root.config(menu=mymenu)

submenu = Menu(mymenu)
#add items to the meni
mymenu.add_cascade(label="File", menu=submenu)

submenu.add_command(label="Project", command=function1)
submenu.add_command(label="Save", command=function1)
#add a separator
submenu.add_separator()
submenu.add_command(label="Exit", command=function1)

#add another menu
newmenu = Menu(mymenu)
mymenu.add_cascade(label="Edit", menu=newmenu)
newmenu.add_command(label="Undo", command=function1)

#create toolbar
toolbar= Frame(root, bg="pink")
insertbutton = Button(toolbar, text="insert", command=function1)
insertbutton.pack(side=LEFT, padx=2, pady=3)

printbutton = Button(toolbar, text="print", command=function1())
printbutton.pack(side=LEFT, padx=2, pady=3)

toolbar.pack(side=TOP, fill=X)

status = Label(root, text="This is the status", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)

root=mainloop()