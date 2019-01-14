#self adjusting Widgets
from tkinter import *

root= Tk()

label1 = Label(root, text="First", bg="red", fg="White")#bg=background color fg=text color
label1.pack(fill=X)#fill=X makes the window self adjusted

#makes the window adjust the Y axe
label2 = Label(root, text="Second", bg="Blue", fg="Green")
label2.pack(side=LEFT, fill=Y)


root.mainloop()