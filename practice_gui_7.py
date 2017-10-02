from tkinter import *

root = Tk()

def leftClick(event):
    print("Hello, my name is Bigfoot!")

def rightClick(event):
    print("Hello, my name is Frankenstein's Monster!")

def middleClick(event):
    print("Hello, my name is the Wolfman!")

#A frame is a black empty container
frame = Frame(root, width=300, height=250) #height and width in pixels
frame.bind("<Button-1>", leftClick)
frame.bind("<Button-2>", middleClick)
frame.bind("<Button-3>", rightClick)
frame.pack()

root.mainloop()
