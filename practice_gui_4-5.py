from tkinter import *

root =Tk()

def leftClick(event):
    print("Hello, my name is BigFoot!")
    
#button_1 = Button(root, text="Print My Name",command=printName, fg="white", bg="pink")
button_1 = Button(root, text="Print My Name",fg="white", bg="pink")
button_1.bind("<Button-1>", leftClick) # "bind()" function takes two parameters, what event
# are you waiting for and what function to call

button_1.pack()

root.mainloop()
