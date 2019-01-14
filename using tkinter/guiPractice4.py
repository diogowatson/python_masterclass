#handling button clicks
from tkinter import *

root = Tk()

#define the code to be executed when button is pressed
def dosomething():
    print("You pressed the button")

button1 = Button(root, text="print",command=dosomething)
button1.pack()

root.mainloop()