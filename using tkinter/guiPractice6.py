#creating drop down menus
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


root=mainloop()