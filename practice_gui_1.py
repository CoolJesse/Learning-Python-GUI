from tkinter import *

root = Tk() #constructor in tkinter class creates blank window, that's what root is
#theLabel = Label(root, text = "Let's get busy!")
#theLabel.pack() # pack widget in first place it will fit on screen

topFrame = Frame(root)
topFrame.pack() #place in main program

bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

button1 = Button(topFrame, text="DO NOT PRESS!", fg="red")
button2 = Button(topFrame, text="Press Me!", fg="purple")
button3 = Button(topFrame, text="Abort", fg="blue")
button4 = Button(bottomFrame, text="Hello!", fg="green")

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)

root.mainloop() # prevents window from closing after program executes once
