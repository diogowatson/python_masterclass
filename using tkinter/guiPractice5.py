#using classes

from tkinter import *

class MyButtons:
    def __init__(self,rootone):
        frame = Frame(rootone)
        frame.pack()
        #buttons
        self.printbutton = Button(frame, text="click here", command=self.printmessage)
        self.printbutton.pack()
        self.quitbutton = Button(frame, text="Exit", command=frame.quit)
        self.quitbutton.pack(side=LEFT)#button going to be in the extreme left

    def printmessage(self):
        print("Button Cliked")

root =Tk()
b = MyButtons(root)

root.mainloop()