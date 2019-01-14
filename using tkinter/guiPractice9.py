#create message box
from tkinter import *
import tkinter.messagebox

root= Tk()
tkinter.messagebox.showinfo("Title", "This is awesome")

#message box that accepts a response
response = tkinter.messagebox.askquestion("Question 1","Do you like coffe")
if response == 'yes':
    print('Here is coffee for you')


root.mainloop()