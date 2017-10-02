#https://www.youtube.com/watch?v=PSm-tq5M-Dc

from tkinter import *

def doNothing():
    print("they do nothing!!!")

root = Tk()

menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="The goggles...", command=doNothing)
subMenu.add_separator()
subMenu.add_command(label="Now...", command=doNothing)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=doNothing)

editMenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Redo", command=doNothing)

root.mainloop()
